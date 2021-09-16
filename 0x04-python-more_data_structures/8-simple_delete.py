#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new = a_dictionary
    if key in a_dictionary:
        del new[key]
    return new
