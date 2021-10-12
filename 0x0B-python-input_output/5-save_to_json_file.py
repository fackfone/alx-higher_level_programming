#!/usr/bin/python3
"""
This module contains a function
that writes an Object to a text file
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function writes an object(Python data structure)
    to a text file using a JSON representation
    """
    with open(filename, 'w+') as file:
        file.read()
        encodedObj = json.JSONEncoder().encode(my_obj)
        file.write(encodedObj)
