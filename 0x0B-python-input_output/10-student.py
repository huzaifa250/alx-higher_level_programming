#!/usr/bin/python3
"""module for class Student."""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student"""
        if attrs is not None and all(isinstance(item, str) for item in attrs):
            res = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    res[k] = v
            return res
        else:
            return self.__dict__
