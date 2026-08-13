# -*- coding: utf-8 -*-

# Copyright (c) 2026 Cisco and/or its affiliates.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)


from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = """
---
author:
    - Cisco Netsec TME (@cisco-netsec-tme)
name: client
short_description: Internal client for FMC
description:
  - Wraps urllib to make specific requests to FMC endpoint and parse the responses.
version_added: "1.0.0"
options:
  host:
    type: str
    description:
      - Specifies the HOST
"""

import json
import http.client
import ssl
import base64
import time

# provided for convenience, should be
LOGIN_PATH = "/api/fmc_platform/v1/auth/generatetoken"
REFRESH_PATH = "/api/fmc_platform/v1/auth/refreshtoken"
AUTH_ERROR_STATUS_CODES = (401, 408)
DEFAULT_MAX_RETRIES = 3


class InternalHttpClientError(Exception):
    def __init__(self, message, status_code):
        super(InternalHttpClientError, self).__init__(message)
        self.status_code = status_code


class InternalHttpClient(object):
    """
    Encapsulates a HTTP client with login flow used to communicate with a REST service over SSL.
    """
    def __init__(
            self,
            host,
            login_url_path=None,
            max_retries=DEFAULT_MAX_RETRIES,
            enable_auth_recovery=True):
        # maintained on login/logout
        self._host = host
        self._login_url_path = login_url_path or LOGIN_PATH
        self._max_retries = max_retries
        self._enable_auth_recovery = enable_auth_recovery
        self.username = None
        self.password = None
        self.access_token = None
        self.refresh_token = None

    def send(self, url_path, data=None, method="GET", headers=None):
        """
        Sends a request to the endpoint and returns the response body.
        """
        request_headers = dict(headers or {})

        for attempt in range(self._max_retries + 1):
            if self.access_token is not None:
                request_headers['X-auth-access-token'] = self.access_token
            else:
                request_headers.pop('X-auth-access-token', None)

            response = self._send_request(url_path, data, method, request_headers)
            response_body = self._parse_response_body(response)
            should_retry = self._handle_error(
                response_body,
                response.status,
                response,
                retry_allowed=attempt < self._max_retries
            )
            if should_retry != 2:
                # return the tuple just like connection.send
                return response, response_body

        raise InternalHttpClientError(
            'Maximum request retries exceeded',
            response.status
        )

    def send_login(self, username, password):
        """
        Sends a login request to the endpoint using basic auth.
        """
        if not self._enable_auth_recovery:
            raise InternalHttpClientError(
                'Username/password login is not supported for bearer-token authentication',
                401
            )

        creds = username + ':' + password
        encoded_creds = base64.b64encode(creds.encode())
        encoded_creds_str = encoded_creds.decode("utf-8")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + encoded_creds_str
        }
        res = self._send_request(self._login_url_path, None, "POST", headers)
        response_body = self._parse_response_body(res)
        if self._is_error_response(response_body, res.status):
            raise InternalHttpClientError(
                self._get_error_message(response_body, res.status),
                res.status
            )

        access_token = res.getheader("X-auth-access-token")
        refresh_token = res.getheader("X-auth-refresh-token")
        if not access_token or not refresh_token:
            raise InternalHttpClientError(
                'FMC login response did not contain authentication tokens',
                res.status
            )

        self.username = username
        self.password = password
        self.access_token = access_token
        self.refresh_token = refresh_token
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }

    def send_refresh_token(self):
        if not self._enable_auth_recovery:
            raise InternalHttpClientError(
                'Token refresh is not supported for bearer-token authentication',
                401
            )

        headers = {
            'Content-Type': 'application/json',
            'X-auth-access-token': self.access_token,
            'X-auth-refresh-token': self.refresh_token
        }
        res = self._send_request(REFRESH_PATH, None, "POST", headers)
        response_body = self._parse_response_body(res)

        error_message = self._get_error_message(response_body, res.status)
        if self._is_error_response(response_body, res.status):
            auth_error = int(res.status) in AUTH_ERROR_STATUS_CODES
            invalid_refresh = 'Invalid refresh token' in error_message
            if auth_error or invalid_refresh:
                return self._send_stored_login()
            raise InternalHttpClientError(error_message, res.status)

        self.access_token = res.getheader("X-auth-access-token")
        self.refresh_token = res.getheader("X-auth-refresh-token")
        if not self.access_token or not self.refresh_token:
            raise InternalHttpClientError(
                'FMC refresh response did not contain authentication tokens',
                res.status
            )
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }

    def _send_stored_login(self):
        if self.username is None or self.password is None:
            raise InternalHttpClientError(
                'FMC authentication expired and no stored credentials are available',
                401
            )
        return self.send_login(self.username, self.password)

    def _send_request(self, url_path, data=None, method="GET", headers=None):
        """
        Sends a request to the endpoint and returns the raw http client response object.
        """
        # adapted from Ansible Connection.send()
        # ex:
        #     connection.send(url, data, method=http_method, headers=BASE_HEADERS)
        method = method.upper()

        timeout = 60 if method == "POST" else 30
        conn = http.client.HTTPSConnection(self._host, timeout=timeout, context=ssl._create_unverified_context())

        conn.request(method, url_path, data, headers)
        # response
        response = conn.getresponse()
        return response

    def _parse_response_body(self, res):
        """
        Parses the raw response and returns the response body
        """
        resdata = res.read()
        if not resdata:
            return {}
        response = resdata.decode("utf-8")
        respobject = json.loads(response)
        return respobject

    def _handle_error(self, response, status_code, raw_response=None, retry_allowed=True):
        """
        Handles an error by parsing the response, and raising an error if found in response body.
        """
        if not self._is_error_response(response, status_code):
            return 0

        msg = self._get_error_message(response, status_code)
        status_code = int(status_code)

        is_auth_status = status_code in AUTH_ERROR_STATUS_CODES
        access_token_invalid = 'Access token invalid' in msg
        refresh_token_invalid = 'Invalid refresh token' in msg
        is_auth_error = is_auth_status or access_token_invalid or refresh_token_invalid
        if is_auth_error:
            if not self._enable_auth_recovery:
                raise InternalHttpClientError(msg, status_code)

            if not retry_allowed:
                raise InternalHttpClientError(
                    'Maximum request retries exceeded: {0}'.format(msg),
                    status_code
                )

            if 'Invalid refresh token' in msg:
                self._send_stored_login()
            elif self.refresh_token:
                self.send_refresh_token()
            else:
                self._send_stored_login()
            return 2

        if status_code == 429:
            if not retry_allowed:
                raise InternalHttpClientError(
                    'Maximum request retries exceeded: {0}'.format(msg),
                    status_code
                )
            retry_after = raw_response.getheader("Retry-After") if raw_response is not None else None
            try:
                time.sleep(int(retry_after))
            except (TypeError, ValueError):
                time.sleep(30)
            return 2

        raise InternalHttpClientError(msg, status_code)

    @staticmethod
    def _is_error_response(response, status_code):
        has_error_body = isinstance(response, dict) and 'error' in response
        return has_error_body or int(status_code) >= 400

    @staticmethod
    def _get_error_message(response, status_code):
        if isinstance(response, dict):
            err = response.get('error')
            if isinstance(err, dict):
                msg = err.get('data')
                if not msg:
                    msg = err.get('message')
                if not msg:
                    msg = iter_messages(err.get('messages'))
                if msg:
                    return str(msg)
            elif err:
                description = response.get('errorDescription')
                if not description:
                    description = response.get('error_description')
                if description:
                    return '{0}: {1}'.format(err, description)
                return str(err)

            msg = response.get('errorMsg') or response.get('message')
            if msg:
                return str(msg)
        return 'HTTP {0} returned without an error message'.format(status_code)


def iter_messages(messages):
    """
    Iterates the messages property in the error object.
    """
    if isinstance(messages, list):
        return ' '.join([m.get('description') or str(m) if isinstance(m, dict) else str(m) for m in messages])
    else:
        return messages
