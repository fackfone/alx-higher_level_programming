#!/usr/bin/python3
"""
This module contains a function
that appends a string at the end
of a text file (UTF8) and
returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    This function appends at the end
    of a text file and returns
    the number of characters added
    """
    with open(filename, 'a+') as file:
        file.read()
        return file.write(text)
