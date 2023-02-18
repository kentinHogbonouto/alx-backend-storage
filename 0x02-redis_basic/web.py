#!/usr/bin/env python3
"""
Tracks the number of times a url is called
"""
import requests
import redis


def get_page(url: str) -> str:
    """
    Retrieves an html page given a url
    """
    cache = redis.Redis()
    # key = f"count:{url}"
    key = "Count"
    print(cache.get(key))
    result = requests.get(url).text
    cache.incr(key)
    cache.setex(url, 10, result)
    return result
