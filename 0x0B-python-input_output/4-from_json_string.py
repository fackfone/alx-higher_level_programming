#!/usr/bin/python3
"""
This module contains a function
that returns an object represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """
    This function returns an object(Python data structure)
    represented by a JSON string
    """
    return json.JSONDecoder().decode(my_str)
