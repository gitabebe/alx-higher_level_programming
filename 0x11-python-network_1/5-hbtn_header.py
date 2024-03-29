#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a URL"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))
