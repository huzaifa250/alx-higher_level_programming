#!/usr/bin/python3
"""Module defines inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    doctest.testfile("1-my_list.txt")
