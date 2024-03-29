#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body"""
import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
