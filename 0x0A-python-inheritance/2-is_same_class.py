#!/usr/bin/python3
"""
A function that returns True if the object
is an instance of the specified class,otherwise
False
"""


def is_same_class(obj, a_class):
    """
    Return True is object is an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
