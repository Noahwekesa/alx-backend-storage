#!/usr/bin/env python3
"""
write string to redis
"""

import redis


class Cache:
    def __init__(self):
        self._redis = redis.Redis()

    def store(self, data: str) -> None:
        self._redis.set("data", data)
