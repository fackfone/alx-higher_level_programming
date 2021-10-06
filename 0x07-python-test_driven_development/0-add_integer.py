#!/usr/bin/python3
"""
The function adds two integers
Return the sum of the numbers to
stdout
"""


def add_integer(a, b=98):
    """
    Computes the sum of two integers
    """
    if a is None:
        raise TypeError("a must be an integer")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
