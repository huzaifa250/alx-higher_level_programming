#!/usr/bin/python3
"""Module defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
