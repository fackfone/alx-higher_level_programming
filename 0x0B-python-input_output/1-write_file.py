#!/usr/bin/python3
"""
This module contains a function
that writes a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    This function writes a text file and returns
    the number of characters written
    """
    with open(filename, 'w+') as file:
        file.read()
        return file.write(text)
