#!/usr/bin/python3
"""defines function to create object from JSON representatin form file"""


import json


def load_from_json_file(filename):
    """creates object from JSON representation in file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
