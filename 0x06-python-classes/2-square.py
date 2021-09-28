#!/usr/bin/python3
"""Definition of the Square class that defines
a square by a private instancec and instatiate
as public variable optionally"""


class Square:
    """A class that defines a square with size instance"""
    def __init__(self, size=0):
            if type(size) != int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
