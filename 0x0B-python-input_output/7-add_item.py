#!/usr/bin/python3
"""This Add all arguments to a Python list and save them to a file."""
import sys
import os

arg_list = sys.argv[1:]

if __name__ == "__main__":
    save_to_json = __import__('5-save_to_json_file').save_to_json
    load_from_json = __import__('6-load_from_json_file').load_from_json

    lst = []
    if os.path.exists('add_item.json'):
        lst = load_JSON('add_item.json')

    save_JSON(lst + arg_list, "add_item.json")
