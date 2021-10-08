#!/usr/bin/python3
"""
The function adds two integers
Return the sum of the numbers to
stdout
"""


def add_integer(a, b=98):
    """
    This function does the addition of 2 arguments
    args:
        a (union[int, float]): first number
        b (union[int, float], optional): second number
    returns:
        the result of the addition
    """
    if (a is None) or (b is None):
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
