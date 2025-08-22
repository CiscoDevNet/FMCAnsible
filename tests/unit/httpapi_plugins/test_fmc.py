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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest

from ansible.errors import AnsibleConnectionFailure
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.six import PY3, BytesIO, StringIO
from ansible.module_utils.six.moves.urllib.error import HTTPError

try:
    from unittest import mock
    from unittest.mock import mock_open, patch
except ImportError:
    # support for python 2.7
    import mock
    from mock import patch, mock_open

from ansible_collections.cisco.fmcansible.plugins.httpapi.fmc import (
    BASE_HEADERS, DEFAULT_API_VERSIONS, TOKEN_PATH_TEMPLATE, HttpApi)
from ansible_collections.cisco.fmcansible.plugins.module_utils.common import (
    HTTPMethod, ResponseParams)
from ansible_collections.cisco.fmcansible.plugins.module_utils.fmc_swagger_client import (
    FmcSwaggerParser, SpecProp)

if PY3:
    BUILTINS_NAME = 'builtins'
else:
    BUILTINS_NAME = '__builtin__'


class FakeFmcHttpApiPlugin(HttpApi):
    def __init__(self, conn):
        super(FakeFmcHttpApiPlugin, self).__init__(conn, False)
        self.hostvars = {
            'token_path': '/testLoginUrl',
            'spec_path': '/testSpecUrl',
            'cdfmc': False,
            'token': None
        }

    def get_option(self, var):
        return self.hostvars.get(var, None)

    def set_option(self, option, value):
        self.hostvars[option] = value


class TestFmcHttpApi(unittest.TestCase):

    def setUp(self):
        self.connection_mock = mock.Mock()
        self.fmc_plugin = FakeFmcHttpApiPlugin(self.connection_mock)
        self.fmc_plugin.access_token = 'ACCESS_TOKEN'
        self.fmc_plugin._load_name = 'httpapi'

    def test_login_should_request_tokens_when_no_refresh_token(self):
        self.connection_mock.send.return_value = self._login_response(
            {'access_token': 'ACCESS_TOKEN', 'refresh_token': 'REFRESH_TOKEN'}
        )

        self.fmc_plugin.login('foo', 'bar')

        assert 'ACCESS_TOKEN' == self.fmc_plugin.access_token
        assert 'REFRESH_TOKEN' == self.fmc_plugin.refresh_token
        # no longer supported in plugin, keeping for historical purposes:
        # assert {'Authorization': 'Bearer ACCESS_TOKEN'} == self.fmc_plugin.connection._auth
        expected_body = json.dumps({'grant_type': 'password', 'username': 'foo', 'password': 'bar'})
        self.connection_mock.send.assert_called_once_with(mock.ANY, expected_body, headers=mock.ANY, method=mock.ANY)

    def test_login_should_update_tokens_when_refresh_token_exists(self):
        self.fmc_plugin.refresh_token = 'REFRESH_TOKEN'
        self.connection_mock.send.return_value = self._login_response(
            {'X-auth-access-token': 'NEW_ACCESS_TOKEN', 'refresh_token': 'NEW_REFRESH_TOKEN'}
        )

        self.fmc_plugin.login('foo', 'bar')

        assert 'NEW_ACCESS_TOKEN' == self.fmc_plugin.access_token
        assert 'NEW_REFRESH_TOKEN' == self.fmc_plugin.refresh_token
        expected_body = json.dumps({'grant_type': 'refresh_token', 'refresh_token': 'REFRESH_TOKEN'})
        self.connection_mock.send.assert_called_once_with(mock.ANY, expected_body, headers=mock.ANY, method=mock.ANY)

    def test_login_should_use_env_variable_when_set(self):
        temp_token_path = self.fmc_plugin.hostvars['token_path']
        self.fmc_plugin.hostvars['token_path'] = '/testFakeLoginUrl'
        self.connection_mock.send.return_value = self._login_response(
            {'access_token': 'ACCESS_TOKEN', 'refresh_token': 'REFRESH_TOKEN'}
        )

        self.fmc_plugin.login('foo', 'bar')

        self.connection_mock.send.assert_called_once_with('/testFakeLoginUrl', mock.ANY, headers=mock.ANY,
                                                          method=mock.ANY)
        self.fmc_plugin.hostvars['token_path'] = temp_token_path

    def test_login_raises_exception_when_no_refresh_token_and_no_credentials(self):
        with self.assertRaises(AnsibleConnectionFailure) as res:
            self.fmc_plugin.login(None, None)
        assert 'Username and password are required' in str(res.exception)

    def test_login_raises_exception_when_invalid_response(self):
        self.connection_mock.send.return_value = self._login_response(
            {'no_access_token': 'ACCESS_TOKEN'},
            apply_base_headers=False
        )

        with self.assertRaises(ConnectionError) as res:
            self.fmc_plugin.login('foo', 'bar')

        assert 'Server returned response without token info during connection authentication' in str(res.exception)

    def test_login_raises_exception_when_http_error(self):
        self.connection_mock.send.side_effect = HTTPError('http://testhost.com', 400, '', {},
                                                          StringIO('{"message": "Failed to authenticate user"}'))

        with self.assertRaises(ConnectionError) as res:
            self.fmc_plugin.login('foo', 'bar')

        assert "Failed to authenticate user" in str(res.exception)

    def test_logout_should_revoke_tokens(self):
        self.fmc_plugin.access_token = 'ACCESS_TOKEN_TO_REVOKE'
        self.fmc_plugin.refresh_token = 'REFRESH_TOKEN_TO_REVOKE'
        self.connection_mock.send.return_value = self._login_response(None)

        self.fmc_plugin.logout()

        assert self.fmc_plugin.access_token is None
        assert self.fmc_plugin.refresh_token is None
        expected_body = json.dumps({'grant_type': 'revoke_token', 'access_token': 'ACCESS_TOKEN_TO_REVOKE',
                                    'token_to_revoke': 'REFRESH_TOKEN_TO_REVOKE'})
        self.connection_mock.send.assert_called_once_with(mock.ANY, expected_body, headers=mock.ANY, method=mock.ANY)

    def test_send_request_should_send_correct_request(self):
        exp_resp = {'id': '123', 'name': 'foo'}
        self.connection_mock.send.return_value = self._connection_response(exp_resp)

        resp = self.fmc_plugin.send_request('/test/{objectId}', HTTPMethod.PUT,
                                            body_params={'name': 'foo'},
                                            path_params={'objectId': '123'},
                                            query_params={'at': 0})

        assert {ResponseParams.SUCCESS: True, ResponseParams.STATUS_CODE: 200,
                ResponseParams.RESPONSE: exp_resp} == resp
        self.connection_mock.send.assert_called_once_with('/test/123?at=0', '{"name": "foo"}', method=HTTPMethod.PUT,
                                                          headers=BASE_HEADERS)

    def test_send_request_should_return_empty_dict_when_no_response_data(self):
        self.connection_mock.send.return_value = self._connection_response(None)

        resp = self.fmc_plugin.send_request('/test', HTTPMethod.GET)

        assert {ResponseParams.SUCCESS: True, ResponseParams.STATUS_CODE: 200, ResponseParams.RESPONSE: {}} == resp
        self.connection_mock.send.assert_called_once_with('/test', None, method=HTTPMethod.GET,
                                                          headers=BASE_HEADERS)

    def test_send_request_should_return_error_info_when_http_error_raises(self):
        self.connection_mock.send.side_effect = HTTPError('http://testhost.com', 500, '', {},
                                                          StringIO('{"errorMessage": "ERROR"}'))

        resp = self.fmc_plugin.send_request('/test', HTTPMethod.GET)

        assert not resp[ResponseParams.SUCCESS]
        assert resp[ResponseParams.STATUS_CODE] == 500
        # assert {ResponseParams.SUCCESS: False, ResponseParams.STATUS_CODE: 500,
        #        ResponseParams.RESPONSE: {'errorMessage': 'ERROR'}} == resp

    def test_send_request_raises_exception_when_invalid_response(self):
        self.connection_mock.send.return_value = self._connection_response('nonValidJson')

        resp = self.fmc_plugin.send_request('/test', HTTPMethod.GET)

        assert not resp[ResponseParams.SUCCESS]
        assert resp[ResponseParams.STATUS_CODE] == 500

    def test_handle_httperror_should_update_tokens_and_retry_on_auth_errors(self):
        self.fmc_plugin.refresh_token = 'REFRESH_TOKEN'
        self.connection_mock.send.return_value = self._login_response(
            {'access_token': 'NEW_ACCESS_TOKEN', 'refresh_token': 'NEW_REFRESH_TOKEN'}
        )

        retry = self.fmc_plugin.handle_httperror(HTTPError('http://testhost.com', 401, '', {}, None))

        assert retry
        assert 'NEW_ACCESS_TOKEN' == self.fmc_plugin.access_token
        assert 'NEW_REFRESH_TOKEN' == self.fmc_plugin.refresh_token

    def test_handle_httperror_should_not_retry_on_non_auth_errors(self):
        assert not self.fmc_plugin.handle_httperror(HTTPError('http://testhost.com', 500, '', {}, None))

    def test_handle_httperror_should_not_retry_when_ignoring_http_errors(self):
        self.fmc_plugin._ignore_http_errors = True
        assert not self.fmc_plugin.handle_httperror(HTTPError('http://testhost.com', 401, '', {}, None))

    @patch('os.path.isdir', mock.Mock(return_value=False))
    def test_download_file(self):
        self.connection_mock.send.return_value = self._connection_response('File content')

        open_mock = mock_open()
        with patch('%s.open' % BUILTINS_NAME, open_mock):
            self.fmc_plugin.download_file('/files/1', '/tmp/test.txt')

        open_mock.assert_called_once_with('/tmp/test.txt', 'wb')
        open_mock().write.assert_called_once_with(b'File content')

    @patch('os.path.isdir', mock.Mock(return_value=True))
    def test_download_file_should_extract_filename_from_headers(self):
        filename = 'test_file.txt'
        response = mock.Mock()
        response.info.return_value = {'Content-Disposition': 'attachment; filename="%s"' % filename}
        dummy, response_data = self._connection_response('File content')
        self.connection_mock.send.return_value = response, response_data

        open_mock = mock_open()
        with patch('%s.open' % BUILTINS_NAME, open_mock):
            self.fmc_plugin.download_file('/files/1', '/tmp/')

        open_mock.assert_called_once_with('/tmp/%s' % filename, 'wb')
        open_mock().write.assert_called_once_with(b'File content')

    @patch('os.path.basename', mock.Mock(return_value='test.txt'))
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.encode_multipart_formdata',
           mock.Mock(return_value=('--Encoded data--', 'multipart/form-data')))
    def test_upload_file(self):
        self.connection_mock.send.return_value = self._connection_response({'id': '123'})

        open_mock = mock_open()
        with patch('%s.open' % BUILTINS_NAME, open_mock):
            resp = self.fmc_plugin.upload_file('/tmp/test.txt', '/files')

        assert {'id': '123'} == resp
        exp_headers = dict(BASE_HEADERS)
        exp_headers['Content-Length'] = len('--Encoded data--')
        exp_headers['Content-Type'] = 'multipart/form-data'
        self.connection_mock.send.assert_called_once_with('/files', '--Encoded data--',
                                                          headers=exp_headers, method=HTTPMethod.POST)
        open_mock.assert_called_once_with('/tmp/test.txt', 'rb')

    @patch('os.path.basename', mock.Mock(return_value='test.txt'))
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.encode_multipart_formdata',
           mock.Mock(return_value=('--Encoded data--', 'multipart/form-data')))
    def test_upload_file_raises_exception_when_invalid_response(self):
        self.connection_mock.send.return_value = self._connection_response('invalidJsonResponse')

        open_mock = mock_open()
        with patch('%s.open' % BUILTINS_NAME, open_mock):
            with self.assertRaises(ConnectionError) as res:
                self.fmc_plugin.upload_file('/tmp/test.txt', '/files')

        assert 'Invalid JSON response' in str(res.exception)

    @patch.object(FmcSwaggerParser, 'parse_spec')
    def test_get_operation_spec(self, parse_spec_mock):
        self.connection_mock.send.return_value = self._connection_response(None)
        parse_spec_mock.return_value = {
            SpecProp.OPERATIONS: {'testOp': 'Specification for testOp'}
        }

        assert 'Specification for testOp' == self.fmc_plugin.get_operation_spec('testOp')
        assert self.fmc_plugin.get_operation_spec('nonExistingTestOp') is None

    @patch.object(FmcSwaggerParser, 'parse_spec')
    def test_get_model_spec(self, parse_spec_mock):
        self.connection_mock.send.return_value = self._connection_response(None)
        parse_spec_mock.return_value = {
            SpecProp.MODELS: {'TestModel': 'Specification for TestModel'}
        }

        assert 'Specification for TestModel' == self.fmc_plugin.get_model_spec('TestModel')
        assert self.fmc_plugin.get_model_spec('NonExistingTestModel') is None

    @patch.object(FmcSwaggerParser, 'parse_spec')
    def test_get_operation_spec_by_model_name(self, parse_spec_mock):
        self.connection_mock.send.return_value = self._connection_response(None)
        operation1 = {'modelName': 'TestModel'}
        op_model_name_is_none = {'modelName': None}
        op_without_model_name = {'url': 'testUrl'}

        parse_spec_mock.return_value = {
            SpecProp.MODEL_OPERATIONS: {
                'TestModel': {
                    'testOp1': operation1,
                    'testOp2': 'spec2'
                },
                'TestModel2': {
                    'testOp10': 'spec10',
                    'testOp20': 'spec20'
                }
            },
            SpecProp.OPERATIONS: {
                'testOp1': operation1,
                'testOp10': {
                    'modelName': 'TestModel2'
                },
                'testOpWithoutModelName': op_without_model_name,
                'testOpModelNameIsNone': op_model_name_is_none
            }
        }

        assert {'testOp1': operation1, 'testOp2': 'spec2'} == self.fmc_plugin.get_operation_specs_by_model_name(
            'TestModel')
        assert None is self.fmc_plugin.get_operation_specs_by_model_name(
            'testOpModelNameIsNone')

        assert None is self.fmc_plugin.get_operation_specs_by_model_name(
            'testOpWithoutModelName')

        assert self.fmc_plugin.get_operation_specs_by_model_name('nonExistingOperation') is None

    def test_get_list_of_supported_api_versions_with_positive_response(self):
        http_response_mock = mock.MagicMock()
        http_response_mock.getvalue.return_value = '{"supportedVersions": ["v1"]}'

        send_mock = mock.MagicMock(return_value=(None, http_response_mock))
        with mock.patch.object(self.fmc_plugin.connection, 'send', send_mock):
            supported_versions = self.fmc_plugin._get_supported_api_versions()
            assert supported_versions == 'v1'

    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_api_token_path', mock.MagicMock(return_value=None))
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_known_token_paths')
    def test_lookup_login_url_with_empty_response(self, get_known_token_paths_mock):
        payload = mock.MagicMock()
        get_known_token_paths_mock.return_value = []
        self.assertRaises(
            ConnectionError,
            self.fmc_plugin._lookup_login_url,
            payload
        )

    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_known_token_paths')
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._send_login_request')
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.display')
    def test_lookup_login_url_with_failed_request(self, display_mock, api_request_mock, get_known_token_paths_mock):
        payload = mock.MagicMock()
        url = mock.MagicMock()
        get_known_token_paths_mock.return_value = [url]
        api_request_mock.side_effect = ConnectionError('Error message')
        self.assertRaises(
            ConnectionError,
            self.fmc_plugin._lookup_login_url,
            payload
        )
        assert display_mock.vvvv.called

    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_api_token_path', mock.MagicMock(return_value=None))
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_known_token_paths')
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._send_login_request')
    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._set_api_token_path')
    def test_lookup_login_url_with_positive_result(self, set_api_token_mock, api_request_mock,
                                                   get_known_token_paths_mock):
        payload = mock.MagicMock()
        url = mock.MagicMock()
        get_known_token_paths_mock.return_value = [url]
        response_mock = mock.MagicMock()
        api_request_mock.return_value = response_mock

        resp = self.fmc_plugin._lookup_login_url(payload)

        set_api_token_mock.assert_called_once_with(url)
        assert resp == response_mock

    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_supported_api_versions')
    def test_get_known_token_paths_with_positive_response(self, get_list_of_supported_api_versions_mock):
        test_versions = ['v1', 'v2']
        get_list_of_supported_api_versions_mock.return_value = test_versions
        result = self.fmc_plugin._get_known_token_paths()
        assert result == [TOKEN_PATH_TEMPLATE.format(version) for version in test_versions]

    @patch('ansible_collections.cisco.fmcansible.plugins.httpapi.fmc.HttpApi._get_supported_api_versions')
    def test_get_known_token_paths_with_failed_api_call(self, get_list_of_supported_api_versions_mock):
        get_list_of_supported_api_versions_mock.side_effect = ConnectionError('test errro message')
        result = self.fmc_plugin._get_known_token_paths()
        assert result == [TOKEN_PATH_TEMPLATE.format(version) for version in DEFAULT_API_VERSIONS]

    def test_set_api_token_path(self):
        url = mock.MagicMock()
        self.fmc_plugin._set_api_token_path(url)
        assert self.fmc_plugin._get_api_token_path() == url

    # helpers
    @staticmethod
    def _connection_response(response, status=200):
        response_mock = mock.Mock()
        response_mock.getcode.return_value = status
        response_text = json.dumps(response) if isinstance(response, dict) else response
        response_data = BytesIO(response_text.encode() if response_text else ''.encode())
        return response_mock, response_data

    @staticmethod
    def _login_response(response_headers, status=200, apply_base_headers=True):
        response_mock = mock.Mock()
        response_mock.getcode.return_value = status
        base_headers = {
            'X-auth-access-token': None,
            'X-auth-refresh-token': None,
            'global': 'e276abec-e0f2-11e3-8169-6d9ed49b625f',
            'DOMAINS': '[{"uuid": "e276abec-e0f2-11e3-8169-6d9ed49b625f", "name":"Global"}]'
        }
        if apply_base_headers and isinstance(response_headers, dict):
            headers_dict = base_headers.copy()
            # rename tokens if needed
            headers_dict['X-auth-access-token'] = response_headers.get('X-auth-access-token') or response_headers.get('access_token') \
                or headers_dict['X-auth-access-token']
            headers_dict['X-auth-refresh-token'] = response_headers.get('X-auth-refresh-token') or response_headers.get('refresh_token') \
                or headers_dict['X-auth-refresh-token']
        else:
            headers_dict = response_headers
        # if they don't pass a dict for headers, let it through and let the errors happen
        response_mock.info.return_value = headers_dict
        response_data = BytesIO(''.encode())
        return response_mock, response_data
