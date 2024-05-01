#!/usr/bin/env python3
''' Redis exercise '''
import redis
from typing import Union, Callable
from uuid import uuid4


class Cache:
    ''' Cache class '''
    def __init__(self) -> None:
        ''' Constructor '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Store method '''
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: callable = None) -> Union[str, bytes, int, float]:
        ''' Get method '''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        ''' Get str method '''
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        ''' Get int method '''
        return self.get(key, int)
