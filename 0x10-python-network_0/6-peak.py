#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
