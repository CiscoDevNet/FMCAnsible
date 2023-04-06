
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import os
import hashlib


def get_hash(obj):
    """
    Creates a hash value for the given object.
    """
    hash_obj = hashlib.sha256(repr(obj).encode('utf-8'))
    return hash_obj.hexdigest()


class ResponseCache:
    def __init__(self, cache_file):
        self.cache_file = cache_file

        if not os.path.exists(self.cache_file):
            with open(self.cache_file, "w") as file:
                json.dump({}, file, indent=2)
        return

    def cache_response(self, name, response_body, host):
        # Load the cached responses from the file
        try:
            with open(self.cache_file, "r") as f:
                cached_responses = json.load(f)
        except FileNotFoundError:
            cached_responses = {}

        if host not in cached_responses:
            cached_responses[host] = {name: response_body}
        elif name not in cached_responses[host]:
            cached_responses[host][name] = response_body
        else:
            flag = False
            if isinstance(response_body, dict):
                flag = True

            # If the key exists, append/extend the response_body to the cached value
            cached_value = [cached_responses[host][name]] if not \
                isinstance(cached_responses[host][name], list) \
                else cached_responses[host][name]

            response_body = [response_body] if not \
                isinstance(response_body, list) else \
                response_body

            combined_list = response_body + cached_value
            unique = []

            # Use a set to check for duplicates based on hash value
            hashes = set()
            for obj in combined_list:
                obj_hash = get_hash(obj)
                if obj_hash not in hashes:
                    unique.append(obj)
                    hashes.add(obj_hash)

            if len(unique) == 1 and flag is True:
                unique = unique[0]

            cached_responses[host][name] = unique

        with open(self.cache_file, "w") as file:
            json.dump(cached_responses, file, indent=2)

    def get_cached_responses(self, hostname):
        try:
            with open(self.cache_file, "r") as file:
                return json.load(file)[f'{hostname}']
        except FileNotFoundError:
            return {}
