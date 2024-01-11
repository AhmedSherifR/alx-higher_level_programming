#!/usr/bin/python3
"""defines function to write JSON representatin of an object to file"""


import json


def save_to_json_file(my_obj, filename):
    """write JSON representation of an object to a file"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
