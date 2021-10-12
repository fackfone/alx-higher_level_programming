#!/usr/bin/python3
"""
This module returns the dictionary description with
simple data structure for JSON serialization of an
object
"""


def class_to_json(obj):
    """
    This function returns the dictionary description
    with simple data structure
    """
    return (obj.__dict__)
