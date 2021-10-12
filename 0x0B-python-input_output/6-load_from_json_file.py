#!/usr/bin/python3
"""
This module contains a function
that creates from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    This function creates an Object from a JSON file
    """
    with open(filename, 'r') as file:
        decoded = json.JSONDecoder().decode(file.read())
        return decoded
