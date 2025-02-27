'''
from __future__ import absolute_import, division, print_function

import unittest
import tempfile
import shutil
import os

__metaclass__ = type

from ansible_collections.cisco.fmcansible.plugins.module_utils.cache import ResponseCache


class TestResponseCache(unittest.TestCase):
    def setUp(self):
        self.cache_dir = tempfile.mkdtemp()
        self.cache_file = os.path.join(self.cache_dir, "test_cache.json")
        self.cache = ResponseCache(self.cache_file)

    def tearDown(self):
        shutil.rmtree(self.cache_dir)

    def test_cache_response(self):
        name = "test_response"
        response_body = {"foo": "bar"}
        host = "www.example.com"
        self.cache.cache_response(name, response_body, host)

        # Check that the response is cached correctly
        cached_responses = self.cache.get_cached_responses(host)
        self.assertIn(name, cached_responses)
        self.assertEqual(cached_responses[name], response_body)

    def test_cache_response_overwrite(self):
        name = "test_response"
        response_body1 = {"foo": "bar"}
        response_body2 = {"foo": "bar"}
        host = "www.example.com"
        self.cache.cache_response(name, response_body1, host)
        self.cache.cache_response(name, response_body2, host)

        # Check that the response is cached correctly
        cached_responses = self.cache.get_cached_responses(host)
        self.assertIn(name, cached_responses)
        self.assertEqual(cached_responses[name], response_body2)

    def test_cache_multiple_responses_dict(self):
        name = "test_response"
        response_body1 = {"foo": "bar"}
        response_body2 = {"baz": "qux"}
        expected_response = [{"baz": "qux"}, {"foo": "bar"}]
        host = "www.example.com"
        self.cache.cache_response(name, response_body1, host)
        self.cache.cache_response(name, response_body2, host)

        # Check that the response is cached correctly
        cached_responses = self.cache.get_cached_responses(host)
        self.assertIn(name, cached_responses)
        self.assertEqual(cached_responses[name], expected_response)

    def test_cache_multiple_responses_list(self):
        name = "test_response"
        response_body1 = [{"foo": "bar"}]
        response_body2 = [{"baz": "qux"}]
        expected_response = [{"baz": "qux"}, {"foo": "bar"}]
        host = "www.example.com"
        self.cache.cache_response(name, response_body1, host)
        self.cache.cache_response(name, response_body2, host)

        # Check that the response is cached correctly
        cached_responses = self.cache.get_cached_responses(host)
        self.assertIn(name, cached_responses)
        self.assertEqual(cached_responses[name], expected_response)

    def test_get_cached_responses(self):
        name1 = "test_response1"
        response_body1 = {"foo": "bar"}
        host1 = "www.example.com"
        self.cache.cache_response(name1, response_body1, host1)

        name2 = "test_response2"
        response_body2 = ["baz", "qux"]
        host2 = "www.example.org"
        self.cache.cache_response(name2, response_body2, host2)

        # Check that the cached responses are returned correctly
        cached_responses1 = self.cache.get_cached_responses(host1)
        self.assertIn(name1, cached_responses1)
        self.assertEqual(cached_responses1[name1], response_body1)

        cached_responses2 = self.cache.get_cached_responses(host2)
        self.assertIn(name2, cached_responses2)
        self.assertEqual(cached_responses2[name2], response_body2)


if __name__ == "__main__":
    unittest.main()
'''
