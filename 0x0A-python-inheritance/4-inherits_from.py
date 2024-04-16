#!/usr/bin/python3
"""Module defines an inherited checking class."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): A class gainst which we are checking whether
        obj is a subclass.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
