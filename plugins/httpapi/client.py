import json
import os
import re
import http.client
import ssl
import base64
from urllib import response
from urllib.parse import urlencode

# provided for convenience, should be
LOGIN_PATH = "/api/fmc_platform/v1/auth/generatetoken"

class InternalHttpClient(object):
    """ 
    Encapsulates a HTTP client with login flow used to communicate with a REST service over SSL.
    """
    def __init__(self, host, login_url_path=None):
        # maintained on login/logout
        #self._access_token = None
        #self._refresh_token = None
        self._host = host
        self._login_url_path = login_url_path or LOGIN_PATH

    def send(self, url_path, data=None, method="GET", headers=None):
        with open('/tmp/log.txt', 'a') as f:
            f.write(f"\n >>>>>url_path: {url_path}")
            f.write(f"\n >>>>>data: {data}")
            f.write(f"\n >>>>>headers: {headers}")
        """ 
        Sends a request to the endpoint and returns the response body.
        """
        print(f'send({url_path}, {data}, {method}, {headers})')
        response = self._send_request(url_path, data, method, headers)
        response_body = self._parse_response_body(response)
        #print('response_body', response_body)
        self._handle_error(response_body)
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
        access_token = res.getheader("X-auth-access-token")
        refresh_token = res.getheader("X-auth-refresh-token")
        return {
          'access_token': access_token,
          'refresh_token': refresh_token
        }
        
    def _send_request(self, url_path, data=None, method="GET", headers=None):
        """ 
        Sends a request to the endpoint and returns the raw http client response object.
        """
        with open('/tmp/log.txt', 'a') as f:
            f.write(f"\n >> _send_request url_path: {url_path}")
            f.write(f"\n >> _send_request data: {data}")
            f.write(f"\n >> _send_request headers: {headers}")

        # adapted from Ansible Connection.send()
        # ex:
        #     connection.send(url, data, method=http_method, headers=BASE_HEADERS)
        method = method.upper()
        conn = http.client.HTTPSConnection(self._host, timeout=5, context=ssl._create_unverified_context())
        # conn.request("POST", "/api/fmc_platform/v1/auth/generatetoken", None, headers)
        try:
            conn.request(method, url_path, data, headers)

            res = conn.getresponse()
            # resdata = res.read()

            # with open('/tmp/log.txt', 'a') as f:
            #     f.write(f"\n resdata: {resdata}")

            # response
            # response = self._get_response(conn)

            # with open('/tmp/log.txt', 'a') as f:
            #         f.write(f"\n send_request got response:")
            return res
        except BaseException as e:
            with open('/tmp/log.txt', 'a') as f:
                f.write(f"\n caught an excpetion: {e}")
    def _get_response(self, conn):
        """ 
        Handles the response.
        """
        res = conn.getresponse()
        return res

    def _parse_response_body(self, res):
        """ 
        Parses the raw response and returns the response body
        """
        resdata = res.read()
        response = resdata.decode("utf-8")
        respobject = json.loads(response)
        return respobject

    def _handle_error(self, response):
        """ 
        Handles an error by parsing the response, and raising an error if found in response body.
        """
        if 'error' in response:
            err = response.get('error')
            msg = err.get('data') or err.get('message') or iter_messages(err.get('messages'))
            #raise ConnectionError(to_text(msg, errors='surrogate_then_replace'), code=code)
            raise Exception(f'FMC Error: {msg}')

def iter_messages(messages):
    """
    Iterates the messages property in the error object.
    """
    if isinstance(messages, list):
        return ' '.join([m.get('description') or str(m) if isinstance(m, dict) else str(m) for m in messages])
    else:
        return messages

if __name__ == '__main__':
    # test login
    host = os.environ.get('FMC_HOST')
    username = os.environ.get('FMC_USERNAME')
    password = os.environ.get('FMC_PASSWORD')
    client = InternalHttpClient(host)
    auth = client.send_login(username, password)
    # get token
    headers = {
      'X-auth-access-token': auth.get('access_token')
    }
    # make test request
    path = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks'
    resp, resp_body = client.send(path, None, method="GET", headers=headers)
    print('response:')
    print(resp_body.getvalue())
    # test with error
    # path = '/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks/fake-guid'
    # try:
    #     resp, resp_body = client.send(path, data=None, "GET", headers)
    #     print('response:')
    #     print(resp_body)
    # except Exception as e:
    #   #foo = e.read()
    #   print(e)
