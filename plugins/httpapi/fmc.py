# -*- coding: utf-8 -*-

# Copyright (c) 2018 Cisco and/or its affiliates.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = """
---
author: Ansible Networking Team
httpapi : fmc
short_description: HttpApi Plugin for Cisco Secure Firewall device
description:
  - This HttpApi plugin provides methods to connect to Cisco Secure Firewall
    devices over a HTTP(S)-based api.
version_added: "1.0.0"
options:
  token_path:
    type: str
    description:
      - Specifies the api token path of the FMC device
    vars:
      - name: ansible_httpapi_fmc_token_path
  spec_path:
    type: str
    description:
      - Specifies the api spec path of the FMC device
    default: '/api/api-explorer/fmc.json'
    vars:
      - name: ansible_httpapi_fmc_spec_path
"""

import json
import os
import re

from ansible import __version__ as ansible_version

from ansible.module_utils.basic import to_text
from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.plugins.httpapi import HttpApiBase
from urllib3 import encode_multipart_formdata
from urllib3.fields import RequestField
from ansible.module_utils.connection import ConnectionError

from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import FmcSwaggerParser, SpecProp, FmcSwaggerValidator
from ansible_collections.cisco.fmcansible.plugins.module_utils.common import HTTPMethod, ResponseParams
try:
    from ansible_collections.cisco.fmcansible.plugins.httpapi.client import InternalHttpClient
except ImportError:
    InternalHttpClient = None

BASE_HEADERS = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'User-Agent': 'FMC Ansible/%s' % ansible_version
}

TOKEN_EXPIRATION_STATUS_CODE = 408
UNAUTHORIZED_STATUS_CODE = 401
API_TOKEN_PATH_OPTION_NAME = 'token_path'
# TOKEN_PATH_TEMPLATE = '/api/fdm/{}/fdm/token'
TOKEN_PATH_TEMPLATE = '/api/fmc_platform/v1/auth/generatetoken'
# GET_API_VERSIONS_PATH = '/api/versions'
GET_API_VERSIONS_PATH = '/info/versions'
DEFAULT_API_VERSIONS = ['v1']

INVALID_API_TOKEN_PATH_MSG = ('The API token path is incorrect. Please, check correctness of '
                              'the `ansible_httpapi_fmc_token_path` variable in the inventory file.')
MISSING_API_TOKEN_PATH_MSG = ('Ansible could not determine the API token path automatically. Please, '
                              'specify the `ansible_httpapi_fmc_token_path` variable in the inventory file.')

try:
    import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class HttpApi(HttpApiBase):
    def __init__(self, connection, use_internal_client=True):
        super(HttpApi, self).__init__(connection)
        self.connection = connection

        self.access_token = None
        self.refresh_token = None
        self._api_spec = None
        self._api_validator = None
        self._ignore_http_errors = False
        self._use_internal_client = use_internal_client
        self._http_client = None

    @property
    def http_client(self):
        # use separate internal client to manage requests (if available)
        if self._http_client is not None:
            return self._http_client
        if InternalHttpClient and self._use_internal_client:
            try:
                host = self.connection.get_option('host')
                self._http_client = InternalHttpClient(host, TOKEN_PATH_TEMPLATE)
            except Exception:
                self._use_internal_client = False
                self._http_client = None
        else:
            self._use_internal_client = False
            self._http_client = None
        return self._http_client

    def login(self, username, password):
        def request_token_payload(username, password):
            return {
                'grant_type': 'password',
                'username': username,
                'password': password
            }

        def refresh_token_payload(refresh_token):
            return {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token
            }

        if self.refresh_token:
            payload = refresh_token_payload(self.refresh_token)
        elif username and password:
            payload = request_token_payload(username, password)
        else:
            raise AnsibleConnectionFailure('Username and password are required for login in absence of refresh token')

        response = self._lookup_login_url(payload)

        # try:
        #     self.refresh_token = response['refresh_token']
        #     self.access_token = response['access_token']
        #     self.connection._auth = {'Authorization': 'Bearer %s' % self.access_token}
        # except KeyError:
        #     raise ConnectionError(
        #         'Server returned response without token info during connection authentication: %s' % response)

        try:
            self.refresh_token = response['X-auth-refresh-token']
            self.access_token = response['X-auth-access-token']
            self.global_domain = response['global']
            self.domains = response['DOMAINS']
            print('don_domains')
            print(self.refresh_token)
            print(self.access_token)
            print(self.global_domain)
            print(self.domains)
            print(type(self.domains))
            global domains_struct
            domains_struct = self.domains
            domains_struct = json.loads(domains_struct)
            print(domains_struct)
            print(type(domains_struct))
            print('don_domains1')
            BASE_HEADERS['X-auth-access-token'] = self.access_token
            print(BASE_HEADERS)
        except KeyError:
            raise ConnectionError(
                'Server returned response without token info during connection authentication: %s' % response)

    def _lookup_login_url(self, payload):
        """ Try to find correct login URL and get api token using this URL.

        :param payload: Token request payload
        :type payload: dict
        :return: token generation response
        """
        preconfigured_token_path = self._get_api_token_path()
        if preconfigured_token_path:
            token_paths = [preconfigured_token_path]
        else:
            token_paths = self._get_known_token_paths()

        for url in token_paths:
            try:
                response = self._send_login_request(payload, url)

            except ConnectionError as e:
                display.vvvv('REST:request to {0} failed because of connection error: {1}'.format(url, e))
                # In the case of ConnectionError caused by HTTPError we should check response code.
                # Response code 400 returned in case of invalid credentials so we should stop attempts to log in and
                # inform the user.
                if hasattr(e, 'http_code') and e.http_code == 400:
                    raise
            else:
                if not preconfigured_token_path:
                    self._set_api_token_path(url)
                return response

        raise ConnectionError(INVALID_API_TOKEN_PATH_MSG if preconfigured_token_path else MISSING_API_TOKEN_PATH_MSG)

    def _send_login_request(self, payload, url):
        self._display(HTTPMethod.POST, 'login', url)
        response, response_data = self._send_auth_request(
            url, json.dumps(payload), method=HTTPMethod.POST, headers=BASE_HEADERS
        )
        response_auth = response.info()
        return response_auth

    def logout(self):
        auth_payload = {
            'grant_type': 'revoke_token',
            'access_token': self.access_token,
            'token_to_revoke': self.refresh_token
        }

        # lookup login url
        urls = self._get_api_token_path()
        if urls:
            token_paths = [urls]
        else:
            token_paths = self._get_known_token_paths()
        url = token_paths[0]

        self._display(HTTPMethod.POST, 'logout', url)
        self._send_auth_request(url, json.dumps(auth_payload), method=HTTPMethod.POST, headers=BASE_HEADERS)
        self.refresh_token = None
        self.access_token = None

    def _require_login(self):
        return self.access_token is None

    def _send_auth_request(self, path, data, **kwargs):
        error_msg_prefix = 'Server returned an error during authentication request'
        return self._send_service_request(path, error_msg_prefix, data=data, **kwargs)

    def _send_service_request(self, path, error_msg_prefix, data=None, **kwargs):
        try:
            self._ignore_http_errors = True
            return self._send(path, data, **kwargs)
        except HTTPError as e:
            # HttpApi connection does not read the error response from HTTPError, so we do it here and wrap it up in
            # ConnectionError, so the actual error message is displayed to the user.
            error_msg = json.loads(to_text(e.read()))
            raise ConnectionError('%s: %s' % (error_msg_prefix, error_msg), http_code=e.code)
        except Exception as e:
            raise ConnectionError('%s: %s' % (error_msg_prefix, e), http_code=500)
        finally:
            self._ignore_http_errors = False

    def update_auth(self, response, response_data):
        # With tokens, authentication should not be checked and updated on each request
        return None

    def send_request(self, url_path, http_method, body_params=None, path_params=None, query_params=None):
        url = construct_url_path(url_path, path_params, query_params)
        data = json.dumps(body_params) if body_params else None

        try:
            self._display(http_method, 'url', url)
            if data:
                self._display(http_method, 'data', data)

            # log in again if access_token not set
            if self._require_login():
                self._login(self.connection.get_option('remote_user'), self.connection.get_option('password'))

            if self.access_token is None and self.refresh_token is None:
                return self._handle_send_error(http_method, "Verify your credentials or check the maximum number of allowed concurrent logins.", 401)

            response, response_data = self._send(url, data, method=http_method, headers=BASE_HEADERS)

            # response_data is bytearray, so convert to string
            value = self._get_response_value(response_data)
            self._display(http_method, 'response', value)

            return {
                ResponseParams.SUCCESS: True,
                ResponseParams.STATUS_CODE: response.getcode(),
                ResponseParams.RESPONSE: self._response_to_json(value)
            }

        # Being invoked via JSON-RPC, this method does not serialize and pass HTTPError correctly to the method caller.
        # Thus, in order to handle non-200 responses, we need to wrap them into a simple structure and pass explicitly.
        except HTTPError as e:
            error_msg = to_text(e.read())
            return self._handle_send_error(http_method, self._response_to_json(error_msg), e.code)
        except Exception as e:
            status_code = getattr(e, 'status_code') if hasattr(e, 'status_code') else 500
            return self._handle_send_error(http_method, e, status_code)

    def upload_file(self, from_path, to_url):
        url = construct_url_path(to_url)
        self._display(HTTPMethod.POST, 'upload', url)
        with open(from_path, 'rb') as src_file:
            rf = RequestField('fileToUpload', src_file.read(), os.path.basename(src_file.name))
            rf.make_multipart()
            body, content_type = encode_multipart_formdata([rf])

            headers = dict(BASE_HEADERS)
            headers['Content-Type'] = content_type
            headers['Content-Length'] = len(body)

            dummy, response_data = self._send(url, data=body, method=HTTPMethod.POST, headers=headers)
            value = self._get_response_value(response_data)
            self._display(HTTPMethod.POST, 'upload:response', value)
            return self._response_to_json(value)

    def download_file(self, from_url, to_path, path_params=None):
        url = construct_url_path(from_url, path_params=path_params)
        self._display(HTTPMethod.GET, 'download', url)
        response, response_data = self._send(url, data=None, method=HTTPMethod.GET, headers=BASE_HEADERS)

        if os.path.isdir(to_path):
            filename = extract_filename_from_headers(response.info())
            to_path = os.path.join(to_path, filename)

        with open(to_path, "wb") as output_file:
            output_file.write(response_data.getvalue())
        self._display(HTTPMethod.GET, 'downloaded', to_path)

    def handle_httperror(self, exc):
        is_auth_related_code = exc.code == TOKEN_EXPIRATION_STATUS_CODE or exc.code == UNAUTHORIZED_STATUS_CODE
        if not self._ignore_http_errors and is_auth_related_code:
            self.connection._auth = None
            self.login(self.connection.get_option('remote_user'), self.connection.get_option('password'))
            return True
        # None means that the exception will be passed further to the caller
        return None

    def _handle_send_error(self, http_method, error_msg, error_code):
        self._display(http_method, 'error', error_msg)
        return {
            ResponseParams.SUCCESS: False,
            ResponseParams.STATUS_CODE: error_code,
            ResponseParams.RESPONSE: error_msg if error_msg is dict else str(error_msg)
        }

    def _send(self, url, data, **kwargs):
        if self.http_client:
            return self.http_client.send(url, data, **kwargs)
        else:
            return self.connection.send(url, data, **kwargs)

    def _login(self, username, password):
        if self.http_client:
            # login via http client
            login_obj = self.http_client.send_login(username, password)
            self.access_token = login_obj['access_token']
            self.refresh_token = login_obj['refresh_token']
            BASE_HEADERS['X-auth-access-token'] = self.access_token
        else:
            # login using default approach
            return self.login(username, password)

    def _display(self, http_method, title, msg=''):
        display.vvvv('REST:{0}:{1}:{2}\n{3}'.format(http_method, self.connection._url, title, msg))

    @staticmethod
    def _get_response_value(response_data):
        """
        Converts the JSON or JSON-RPC response to string.
        """
        if response_data is None:
            return ''
        try:
            return to_text(response_data.getvalue())
        except AttributeError:
            pass
        return json.dumps(response_data)

    def _get_api_spec_path(self):
        return self.get_option('spec_path')

    def _get_known_token_paths(self):
        """Generate list of token generation urls based on list of versions supported by device(if exposed via API) or
        default list of API versions.

        :returns: list of token generation urls
        :rtype: generator
        """
        try:
            api_versions = self._get_supported_api_versions()
        except ConnectionError:
            # API versions API is not supported we need to check all known version
            api_versions = DEFAULT_API_VERSIONS

        return [TOKEN_PATH_TEMPLATE.format(version) for version in api_versions]

    def _get_supported_api_versions(self):
        """
        Fetch list of API versions supported by device.

        :return: list of API versions suitable for device
        :rtype: list
        """
        # the API only supports v1
        return "v1"

    def _get_api_token_path(self):
        return self.get_option(API_TOKEN_PATH_OPTION_NAME)

    def _set_api_token_path(self, url):
        return self.set_option(API_TOKEN_PATH_OPTION_NAME, url)

    @staticmethod
    def _response_to_json(response_text):
        try:
            return json.loads(response_text) if response_text else {}
        # JSONDecodeError only available on Python 3.5+
        except getattr(json.decoder, 'JSONDecodeError', ValueError):
            raise ConnectionError('Invalid JSON response: %s' % response_text)

    def get_operation_spec(self, operation_name):
        return self.api_spec[SpecProp.OPERATIONS].get(operation_name, None)

    def get_operation_specs_by_model_name(self, model_name):
        if model_name:
            return self.api_spec[SpecProp.MODEL_OPERATIONS].get(model_name, None)
        else:
            return None

    def get_model_spec(self, model_name):
        return self.api_spec[SpecProp.MODELS].get(model_name, None)

    def validate_data(self, operation_name, data):
        return self.api_validator.validate_data(operation_name, data)

    def validate_query_params(self, operation_name, params):
        return self.api_validator.validate_query_params(operation_name, params)

    def validate_path_params(self, operation_name, params):
        return self.api_validator.validate_path_params(operation_name, params)

    @property
    def api_spec(self):
        if self._api_spec is None:
            spec_path_url = self._get_api_spec_path()
            response = (self.send_request(url_path=spec_path_url, http_method=HTTPMethod.GET))
            if response[ResponseParams.SUCCESS]:
                self._api_spec = FmcSwaggerParser().parse_spec(response[ResponseParams.RESPONSE])
            else:
                raise ConnectionError('Failed to download API specification. Status code: %s. Response: %s' % (
                    response[ResponseParams.STATUS_CODE], (response[ResponseParams.RESPONSE]).encode('utf8')))
        return self._api_spec

    @property
    def api_validator(self):
        if self._api_validator is None:
            self._api_validator = FmcSwaggerValidator(self.api_spec)
        return self._api_validator


def construct_url_path(path, path_params=None, query_params=None):
    url = path
    if path_params:
        url = url.format(**path_params)
    # if path_params:
    #     if 'domainname' in path_params:
    #         for domain_model in domains_struct:
    #             if domain_model['name'].lower() == path_params['domainname'].lower():
    #                 path_params['domainUUID'] = domain_model['uuid']
    #                 del path_params['domainname']
    #                 break
    #     url = url.format(**path_params)
    if query_params:
        url += "?" + urlencode(query_params)
    return url


def extract_filename_from_headers(response_info):
    content_header_regex = r'attachment; ?filename="?([^"]+)'
    match = re.match(content_header_regex, response_info.get('Content-Disposition'))
    if match:
        return match.group(1)
    else:
        raise ValueError("No appropriate Content-Disposition header is specified.")
