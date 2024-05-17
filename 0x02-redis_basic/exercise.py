#!/usr/bin/env python3
"""
Redis
"""

import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from sys import byteorder
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts number of calls to a class method
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper for method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Class for methods that operate a caching system
    """

    def __init__(self):
        """Instance of Redis db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Creates key and stores it with data
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """
        Returns data converted to desired format
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        return int.from_bytes(data, byteorder)
