#!/usr/bin/env python3
''' Redis exercise '''
import redis
from typing import Union
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
