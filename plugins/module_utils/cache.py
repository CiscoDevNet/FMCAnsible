import os, json

class ResponseCache:
    def __init__(self, cache_file):
        self.cache_file = cache_file

        if not os.path.exists(self.cache_file):
            with open(self.cache_file, "w") as f:
                json.dump({}, f, indent=2)

    def cache_response(self, name, response_body, is_loop_block=False):
        # Load the cached responses from the file
        try:
            with open(self.cache_file, "r") as f:
                cached_responses = json.load(f)
        except FileNotFoundError:
            cached_responses = {}

        if is_loop_block:
            if name not in cached_responses:
            # If the key doesn't exist
                cached_responses[name] = response_body
            else:
            # If the key exists, append/extend the response_body to the cached value
                cached_value = cached_responses[name]
                if isinstance(cached_value, dict):
                    # If the cached value is a dict, convert it to a list and append the new response body
                    cached_responses[name] = [cached_value, response_body] if isinstance(response_body, dict) else [cached_value] + response_body
                elif isinstance(cached_value, list):
                    # If the cached value is a list, append/extend the new response body to the list
                    if isinstance(response_body, list):
                        cached_responses[name].extend(response_body)
                    else:
                        cached_responses[name].append(response_body)
        else:
            return
        
        with open(self.cache_file, "w") as f:
            json.dump(cached_responses, f, indent=2)

    def get_cached_responses(self, is_loop_block=False):
        if is_loop_block:
            try:
                with open(self.cache_file, "r") as f:
                    return json.load(f)
            except FileNotFoundError:
                return {}
        else:
            return {}