#!/usr/bin/python3
"""
This module contains a script that adds
all arguments to a Python list, and then
save them to a file
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

listArg = list(sys.argv[1:])
try:
    data = load_from_json_file("add_item.json")
except Exception:
    data = []

data.extend(listArg)
save_to_json_file(data, "add_item.json")
