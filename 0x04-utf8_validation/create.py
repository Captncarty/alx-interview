#!/usr/bin/env python3
"""
Generate an extended class to put and get stored cached information
"""


from base_caching import BaseCaching

class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()


    def put(self, key, value):
        """
        add key and value to cache {}
        """
        if key is None and value is None:
            return
        
        self.cache_data[key] = value

    def get(self, key):
        """
        get stored key-values
        """
        if key is None and key not in self.cache_data.keys():
            return None
        
        return self.cache_data[key]
