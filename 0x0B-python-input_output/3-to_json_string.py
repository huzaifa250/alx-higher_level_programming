#!/usr/bin/python3
"""module to convert data usuing json"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string object."""
    return json.dumps(my_obj)
