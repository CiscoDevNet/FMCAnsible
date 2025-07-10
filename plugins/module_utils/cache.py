"""
Cache module for Cisco FMC Ansible modules.

This module provides a response cache to avoid redundant API calls.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os
import json


class ResponseCache:
    """
    A file-based cache for storing responses from FMC API calls.
    This helps reduce redundant API calls during a playbook run.
    """

    def __init__(self, cache_file):
        """
        Initialize the cache with a specific file path.

        Args:
            cache_file (str): Path to the file where cache data will be stored
        """
        self.cache_file = cache_file
        self._cache = {}
        self._load_cache()

    def _load_cache(self):
        """
        Load the cache from the cache file if it exists.
        """
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    self._cache = json.load(f)
            except (json.JSONDecodeError, IOError):
                self._cache = {}
        else:
            self._cache = {}

    def _save_cache(self):
        """
        Save the cache to the cache file.
        """
        try:
            cache_dir = os.path.dirname(self.cache_file)
            if not os.path.exists(cache_dir) and cache_dir:
                os.makedirs(cache_dir)

            with open(self.cache_file, 'w') as f:
                json.dump(self._cache, f)
        except IOError:
            pass  # Silently fail if we can't write to the cache file

    def cache_response(self, name, response_body, host):
        """
        Cache a response for a given name and host.

        If a response with the same name already exists:
        - If both responses are identical dictionaries, the new one replaces the old one
        - If they are different dictionaries or different types, combine them into a list

        Args:
            name (str): Name identifier for the response
            response_body (dict/list): The response data to cache
            host (str): The host identifier
        """
        if host not in self._cache:
            self._cache[host] = {}

        if name in self._cache[host]:
            existing_response = self._cache[host][name]

            # If both are dictionaries, check if they are the same
            if (isinstance(existing_response, dict) and
                    isinstance(response_body, dict)):

                # If dictionaries are different, combine them into a list
                if existing_response != response_body:
                    self._cache[host][name] = [response_body, existing_response]
                else:
                    # If dictionaries are the same, replace with the new one
                    self._cache[host][name] = response_body
            else:
                # Convert existing to list if it's not already
                if not isinstance(existing_response, list):
                    existing_response = [existing_response]

                # Convert new response to list if it's not already
                if not isinstance(response_body, list):
                    new_responses = [response_body]
                else:
                    new_responses = response_body

                # Combine the lists
                self._cache[host][name] = new_responses + existing_response
        else:
            self._cache[host][name] = response_body

        self._save_cache()

    def get_cached_responses(self, host):
        """
        Get all cached responses for a host.

        Args:
            host (str): The host identifier

        Returns:
            dict: Dictionary of cached responses for the host, or empty dict if none
        """
        return self._cache.get(host, {})

    def clear(self):
        """
        Clear all items from the cache.
        """
        self._cache = {}
        self._save_cache()
