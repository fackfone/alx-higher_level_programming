#!/usr/bin/python3
"""
This module contains a function
that reads a text file (UTF8) and 
prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads a text file and prints
    it to stdout
    """
    with open(filename, 'r') as file:
        print(file.read(), end="")
