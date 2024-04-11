#!/usr/bin/python3
"""Module defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    only with attribute 'first_name'.
    """

    __slots__ = ["first_name"]
