#!/usr/bin/env python3
"""fifo cache class script"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """simple fifo cache class"""

    def __init__(self):
        """constructor method"""
        super().__init__()

    def put(self, key, item):
        """method to put (add) in the dict"""
        if not (key and item):
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            keys = list(self.cache_data)
            self.cache_data.pop(keys[0])
            print(f"DISCARD: {keys[0]}")

        self.cache_data[key] = item

    def get(self, key):
        """get an item from the cache"""
        return self.cache_data.get(key, None)
