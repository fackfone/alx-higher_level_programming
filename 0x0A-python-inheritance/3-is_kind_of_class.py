#!/usr/bin/python3
"""
A function that returns True if the object
if is an instance of the specified class,otherwise
False
"""


def is_kind_of_class(obj, a_class):
    """
    Return True is object is an instance of the specified class
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
