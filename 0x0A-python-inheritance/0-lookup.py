#!/usr/bin/python3
"""module for lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
