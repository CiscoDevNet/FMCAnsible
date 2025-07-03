"""
Cache module for Cisco FMC Ansible modules.

This module provides a response cache to avoid redundant API calls.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ResponseCache:
    """
    A simple cache for storing responses from FMC API calls.
    This helps reduce redundant API calls during a playbook run.
    """

    def __init__(self):
        self._cache = {}

    def get(self, key):
        """
        Get a cached response by key.

        Args:
            key (str): The cache key.

        Returns:
            The cached response or None if not found.
        """
        return self._cache.get(key)

    def set(self, key, value):
        """
        Store a response in the cache.

        Args:
            key (str): The cache key.
            value: The response data to cache.

        Returns:
            None
        """
        self._cache[key] = value

    def has(self, key):
        """
        Check if a key exists in the cache.

        Args:
            key (str): The cache key.

        Returns:
            bool: True if the key exists, False otherwise.
        """
        return key in self._cache

    def clear(self):
        """
        Clear all items from the cache.

        Returns:
            None
        """
        self._cache = {}

    def __len__(self):
        """
        Get the number of items in the cache.

        Returns:
            int: The number of items in the cache.
        """
        return len(self._cache)
