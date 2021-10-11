#!/usr/bin/python3
"""
A function that returns True if the object
if is an instance of the class that inherited,otherwise
False
"""


def inherits_from(obj, a_class):
    """
    Return True is object is an instance of the specified class
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
