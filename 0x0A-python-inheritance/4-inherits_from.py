#!/usr/bin/python3

"""module for inherits_from function."""


def inherits_from(obj, a_class):
    """hecks if an object is an inherited instance of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
