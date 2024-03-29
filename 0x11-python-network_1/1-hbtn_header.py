#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a URL."""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info()['X-Request-Id'])
