#!/usr/bin/python3
"""script to add all arguments to a Python list and save to a file"""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
json_list = []

if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for line in argv[1:]:
    json_list.append(line)

save_to_json_file(json_list, filename)
