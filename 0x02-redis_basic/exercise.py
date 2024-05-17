#!/usr/bin/env python3
"""
write string to redis
"""

import redis
import uuid
from typing import Optional, Union, Callable


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable[[bytes], Union[str, int]]] = None
    ) -> Optional[Union[str, int]]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value.decode()

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, lambda x: x.decode())

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, lambda x: int(x))
