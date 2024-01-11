#!/usr/bin/python3
"""defines function to return object from JSON"""


import json


def from_json_string(my_str):
    """returns object from JSON"""
    return json.loads(my_str)
