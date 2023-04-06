from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import json
import unittest
from ansible_collections.cisco.fmcansible.plugins.module_utils.cache import ResponseCache


class TestResponseCache(unittest.TestCase):
    def setUp(self):
        self.cache_file = "/tmp/test_cache.json"
        self.cache = ResponseCache(self.cache_file)

    def tearDown(self):
        os.remove(self.cache_file)

    def test_cache_response(self):
        # Test caching a response for a non-loop block
        self.cache.cache_response("test_key", {"test": "value"})
        hostname = "default"
        with open(self.cache_file, "r") as f:
            cached_responses = json.load(f)
            self.assertEqual(cached_responses, {})

        # Test caching a response for a loop block
        self.cache.cache_response("loop_key", {"key": "value"}, hostname)
        with open(self.cache_file, "r") as f:
            cached_responses = json.load(f)
            expected_cached_responses = {"loop_key": {"key": "value"}}
            self.assertEqual(cached_responses, expected_cached_responses)

        # Test appending to a cached response for a loop block
        self.cache.cache_response("loop_key", {"new": "value"}, hostname)
        with open(self.cache_file, "r") as f:
            cached_responses = json.load(f)
            expected_cached_responses = {"loop_key": [{"key": "value"}, {"new": "value"}]}
            self.assertEqual(cached_responses, expected_cached_responses)

    def test_get_cached_responses(self):
        hostname = "default"
        # Test getting cached responses for a non-loop block
        cached_responses = self.cache.get_cached_responses()
        self.assertEqual(cached_responses, {})

        # Test getting cached responses for a loop block
        self.cache.cache_response("loop_key", {"loop": "value"}, hostname)
        cached_responses = self.cache.get_cached_responses(hostname)
        expected_cached_responses = {"loop_key": {"loop": "value"}}
        self.assertEqual(cached_responses, expected_cached_responses)
