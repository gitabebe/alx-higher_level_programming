#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email"""
import sys
import requests


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
