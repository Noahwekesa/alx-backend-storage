#!/usr/bin/env python3
"""
write string to redis
"""

import redis
import functools
import uuid
from typing import Optional, Union, Callable


def count_calls(method: Callable) -> Callable:
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data):
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
