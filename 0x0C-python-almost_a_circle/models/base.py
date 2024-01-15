#!/usr/bin/python3

"""
module implements `base` class of all other classes in the project
the goal is to manage id attribute in all future classes
"""


class Base:
    """Base model.

    Represents the "base" for all other classes in project.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The id of the new Base whenever obj created.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
