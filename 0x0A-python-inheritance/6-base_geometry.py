#!/usr/bin/python3
"""Module defines a base geometry class"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
