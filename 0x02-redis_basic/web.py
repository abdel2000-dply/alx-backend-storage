#!/usr/bin/python3
''' Redis exercise '''
import redis
import requests

r = redis.Redis()


def get_page(url: str) -> str:
    ''' Get page '''
    page_key = f"page:{url}"
    count_key = f"count:{url}"

    if r.get(page_key):
        r.incr(count_key)
        return r.get(page_key).decode('utf-8')

    response = requests.get(url)
    r.setex(page_key, 10, response.text)
    r.set(count_key, 1)
    return response.text
