#!/usr/bin/python3
''' Redis exercise '''
import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    ''' Get page '''
    if r.get(f"count:{url}"):
        r.incr(f"count:{url}")
        return r.get(url).decode('utf-8')

    response = requests.get(url)
    r.setex(url, 10, response.text)
    r.set(f"count:{url}", 1)
    return response.text
