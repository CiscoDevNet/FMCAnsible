from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import unittest

try:
    from unittest import mock
except ImportError:
    import mock

from ansible_collections.cisco.fmcansible.plugins.httpapi.client import (
    InternalHttpClient, InternalHttpClientError, LOGIN_PATH, REFRESH_PATH)


class FakeHttpResponse(object):
    def __init__(self, status, body=None, headers=None):
        self.status = status
        self._body = body
        self._headers = headers or {}

    def read(self):
        if self._body is None:
            return b''
        if isinstance(self._body, bytes):
            return self._body
        return json.dumps(self._body).encode('utf-8')

    def getheader(self, name):
        return self._headers.get(name)


class TestInternalHttpClient(unittest.TestCase):
    def test_send_refresh_token_uses_raw_response_status_and_headers(self):
        client = InternalHttpClient('fmc.example.com')
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        refresh_response = FakeHttpResponse(
            204,
            headers={
                'X-auth-access-token': 'NEW_ACCESS',
                'X-auth-refresh-token': 'NEW_REFRESH'
            }
        )

        with mock.patch.object(client, '_send_request', return_value=refresh_response) as send_request:
            result = client.send_refresh_token()

        send_request.assert_called_once_with(
            REFRESH_PATH,
            None,
            'POST',
            {
                'Content-Type': 'application/json',
                'X-auth-access-token': 'OLD_ACCESS',
                'X-auth-refresh-token': 'OLD_REFRESH'
            }
        )
        self.assertEqual('NEW_ACCESS', client.access_token)
        self.assertEqual('NEW_REFRESH', client.refresh_token)
        self.assertEqual({'access_token': 'NEW_ACCESS', 'refresh_token': 'NEW_REFRESH'}, result)

    def test_send_refreshes_token_and_returns_retried_response(self):
        client = InternalHttpClient('fmc.example.com')
        client.username = 'user'
        client.password = 'password'
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        expired_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Access token invalid'
                }
            }
        )
        refresh_response = FakeHttpResponse(
            204,
            headers={
                'X-auth-access-token': 'NEW_ACCESS',
                'X-auth-refresh-token': 'NEW_REFRESH'
            }
        )
        success_response = FakeHttpResponse(200, {'items': []})

        with mock.patch.object(
                client,
                '_send_request',
                side_effect=[expired_response, refresh_response, success_response]) as send_request:
            response, response_body = client.send('/api/test', method='GET', headers={})

        self.assertEqual(success_response, response)
        self.assertEqual({'items': []}, response_body)
        self.assertEqual(3, send_request.call_count)
        self.assertEqual('NEW_ACCESS', send_request.call_args_list[-1][0][3]['X-auth-access-token'])

    def test_invalid_refresh_token_falls_back_to_login(self):
        client = InternalHttpClient('fmc.example.com')
        client.username = 'user'
        client.password = 'password'
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        invalid_refresh_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Invalid refresh token'
                }
            }
        )
        login_response = FakeHttpResponse(
            204,
            headers={
                'X-auth-access-token': 'LOGIN_ACCESS',
                'X-auth-refresh-token': 'LOGIN_REFRESH'
            }
        )

        with mock.patch.object(
                client,
                '_send_request',
                side_effect=[invalid_refresh_response, login_response]) as send_request:
            result = client.send_refresh_token()

        self.assertEqual(2, send_request.call_count)
        self.assertEqual(LOGIN_PATH, send_request.call_args_list[-1][0][0])
        self.assertEqual('LOGIN_ACCESS', client.access_token)
        self.assertEqual('LOGIN_REFRESH', client.refresh_token)
        self.assertEqual(
            {'access_token': 'LOGIN_ACCESS', 'refresh_token': 'LOGIN_REFRESH'},
            result
        )

    def test_invalid_refresh_token_raises_when_fallback_login_fails(self):
        client = InternalHttpClient('fmc.example.com')
        client.username = 'user'
        client.password = 'password'
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        invalid_refresh_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Invalid refresh token'
                }
            }
        )
        failed_login_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Authentication failed'
                }
            }
        )

        with mock.patch.object(
                client,
                '_send_request',
                side_effect=[invalid_refresh_response, failed_login_response]):
            with self.assertRaises(InternalHttpClientError) as raised:
                client.send_refresh_token()

        self.assertEqual(401, raised.exception.status_code)
        self.assertEqual('Authentication failed', str(raised.exception))
        self.assertEqual('OLD_ACCESS', client.access_token)
        self.assertEqual('OLD_REFRESH', client.refresh_token)

    def test_send_relogs_and_retries_when_refresh_token_is_invalid(self):
        client = InternalHttpClient('fmc.example.com')
        client.username = 'user'
        client.password = 'password'
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        expired_access_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Access token invalid'
                }
            }
        )
        invalid_refresh_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Invalid refresh token'
                }
            }
        )
        login_response = FakeHttpResponse(
            204,
            headers={
                'X-auth-access-token': 'LOGIN_ACCESS',
                'X-auth-refresh-token': 'LOGIN_REFRESH'
            }
        )
        success_response = FakeHttpResponse(200, {'items': []})

        with mock.patch.object(
                client,
                '_send_request',
                side_effect=[
                    expired_access_response,
                    invalid_refresh_response,
                    login_response,
                    success_response
                ]) as send_request:
            response, response_body = client.send('/api/test', headers={})

        self.assertEqual(success_response, response)
        self.assertEqual({'items': []}, response_body)
        self.assertEqual('LOGIN_ACCESS', client.access_token)
        self.assertEqual('LOGIN_REFRESH', client.refresh_token)
        self.assertEqual(4, send_request.call_count)
        self.assertEqual(
            'LOGIN_ACCESS',
            send_request.call_args_list[-1][0][3]['X-auth-access-token']
        )

    def test_bodyless_401_refreshes_token_and_retries_request(self):
        client = InternalHttpClient('fmc.example.com')
        client.username = 'user'
        client.password = 'password'
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        unauthorized_response = FakeHttpResponse(401)
        refresh_response = FakeHttpResponse(
            204,
            headers={
                'X-auth-access-token': 'NEW_ACCESS',
                'X-auth-refresh-token': 'NEW_REFRESH'
            }
        )
        success_response = FakeHttpResponse(200, {'items': []})

        with mock.patch.object(
                client,
                '_send_request',
                side_effect=[unauthorized_response, refresh_response, success_response]):
            response, response_body = client.send('/api/test', headers={})

        self.assertEqual(success_response, response)
        self.assertEqual({'items': []}, response_body)
        self.assertEqual('NEW_ACCESS', client.access_token)
        self.assertEqual('NEW_REFRESH', client.refresh_token)

    def test_send_stops_after_maximum_authentication_retries(self):
        client = InternalHttpClient('fmc.example.com', max_retries=2)
        client.username = 'user'
        client.password = 'password'
        client.access_token = 'OLD_ACCESS'
        client.refresh_token = 'OLD_REFRESH'
        unauthorized_response = FakeHttpResponse(
            401,
            {
                'error': {
                    'message': 'Access token invalid'
                }
            }
        )
        refresh_response = FakeHttpResponse(
            204,
            headers={
                'X-auth-access-token': 'NEW_ACCESS',
                'X-auth-refresh-token': 'NEW_REFRESH'
            }
        )

        with mock.patch.object(
                client,
                '_send_request',
                side_effect=[
                    unauthorized_response,
                    refresh_response,
                    unauthorized_response,
                    refresh_response,
                    unauthorized_response
                ]) as send_request:
            with self.assertRaises(InternalHttpClientError) as raised:
                client.send('/api/test', headers={})

        self.assertEqual(401, raised.exception.status_code)
        self.assertIn('Maximum request retries exceeded', str(raised.exception))
        self.assertEqual(5, send_request.call_count)

    def test_bodyless_non_auth_http_error_is_raised(self):
        client = InternalHttpClient('fmc.example.com')
        response = FakeHttpResponse(500)

        with mock.patch.object(client, '_send_request', return_value=response):
            with self.assertRaises(InternalHttpClientError) as raised:
                client.send('/api/test', headers={})

        self.assertEqual(500, raised.exception.status_code)
        self.assertEqual(
            'HTTP 500 returned without an error message',
            str(raised.exception)
        )

    def test_send_stops_after_maximum_rate_limit_retries(self):
        client = InternalHttpClient('fmc.example.com', max_retries=1)
        rate_limited_response = FakeHttpResponse(
            429,
            {
                'error': {
                    'message': 'Rate limit exceeded'
                }
            },
            headers={'Retry-After': '0'}
        )

        with mock.patch.object(
                client,
                '_send_request',
                return_value=rate_limited_response) as send_request:
            with mock.patch(
                    'ansible_collections.cisco.fmcansible.plugins.httpapi.client.time.sleep') as sleep:
                with self.assertRaises(InternalHttpClientError) as raised:
                    client.send('/api/test', headers={})

        self.assertEqual(429, raised.exception.status_code)
        self.assertIn('Maximum request retries exceeded', str(raised.exception))
        self.assertEqual(2, send_request.call_count)
        sleep.assert_called_once_with(0)


if __name__ == '__main__':
    unittest.main()
