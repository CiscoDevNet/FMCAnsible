# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cisco and/or its affiliates.
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
from urllib import response
# from urllib.parse import urlencode
import time

# provided for convenience, should be
LOGIN_PATH = "/api/fmc_platform/v1/auth/generatetoken"
REFRESH_PATH = "/api/fmc_platform/v1/auth/refreshtoken"


class InternalHttpClientError(Exception):
    def __init__(self, message, status_code):
        super(InternalHttpClientError, self).__init__(message)
        self.status_code = status_code


class InternalHttpClient(object):
    """
    Encapsulates a HTTP client with login flow used to communicate with a REST service over SSL.
    """
    def __init__(self, host, login_url_path=None):
        # maintained on login/logout
        self._host = host
        self._login_url_path = login_url_path or LOGIN_PATH
        self.username = None
        self.password = None
        self.access_token = None
        self.refresh_token = None

    def send(self, url_path, data=None, method="GET", headers=None):
        """
        Sends a request to the endpoint and returns the response body.
        """
        if headers is not None and self.access_token is not None:
            headers['X-auth-access-token'] = self.access_token

        response = self._send_request(url_path, data, method, headers)
        response_body = self._parse_response_body(response)
        if self._handle_error(response_body, response.status) == 2:
            # Retry send
            self.send(url_path, data, method, headers)
        # return the tuple just like connection.send
        return response, response_body

    def send_login(self, username, password):
        """
        Sends a login request to the endpoint using basic auth.
        """
        creds = username + ':' + password
        encoded_creds = base64.b64encode(creds.encode())
        encoded_creds_str = encoded_creds.decode("utf-8")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + encoded_creds_str
        }
        res = self._send_request(self._login_url_path, None, "POST", headers)

        self.username = username
        self.password = password
        self.access_token = res.getheader("X-auth-access-token")
        self.refresh_token = res.getheader("X-auth-refresh-token")
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token
        }

    def send_refresh_token(self):
        headers = {
            'Content-Type': 'application/json',
            'X-auth-access-token': self.access_token,
            'X-auth-refresh-token': self.refresh_token
        }
        response_body = self._send_request(REFRESH_PATH, None, "POST", headers)
        self._handle_error(response_body, response.status)

        self.access_token = response_body.getheader("X-auth-access-token")
        self.refresh_token = response_body.getheader("X-auth-refresh-token")

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
        response = resdata.decode("utf-8")
        respobject = json.loads(response)
        return respobject

    def _handle_error(self, response, status_code):
        """
        Handles an error by parsing the response, and raising an error if found in response body.
        """
        if 'error' not in response:
            return 0

        err = response.get('error')
        msg = err.get('data') or err.get('message') or iter_messages(err.get('messages'))

        if 'Access token invalid' in msg:
            self.send_refresh_token()
            return 2

        if 'Invalid refresh token' in msg:
            self.send_login(self.username, self.password)
            return 2

        if int(status_code) == 429:
            retry_after = response.getheader("Retry-After")
            try:
                time.sleep(int(retry_after))
            except (TypeError, ValueError):
                time.sleep(30)
            return 2

        # raise ConnectionError(to_text(msg, errors='surrogate_then_replace'), code=code)
        # raise InternalHttpClientError('FMC Error: {0}'.format(msg), status_code)
        raise InternalHttpClientError(msg, status_code)


def iter_messages(messages):
    """
    Iterates the messages property in the error object.
    """
    if isinstance(messages, list):
        return ' '.join([m.get('description') or str(m) if isinstance(m, dict) else str(m) for m in messages])
    else:
        return messages
