#!/usr/bin/env python3
''' Redis exercise '''
from functools import wraps
import redis
from typing import Union, Callable, Optional
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    ''' Count calls decorator '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper '''
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    ''' Call history decorator '''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        ''' Wrapper '''
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(data))
        return data
    return wrapper


class Cache:
    ''' Cache class '''
    def __init__(self) -> None:
        ''' Constructor '''
        self._redis = redis.Redis()
        # self._redis = redis.Redis(decode_responses=True)/we can use this too
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store method '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: callable = None) -> Optional[Union[str, bytes, int, float]]:
        ''' Get method '''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        ''' Get str method '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        ''' Get int method '''
        return self.get(key, int)
