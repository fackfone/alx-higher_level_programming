#!/usr/bin/python3
"""Definition of a Square class which defines a
square object with attributes and also allows
to handle getter and setter functions pythonically"""


class Square:
    """A class that defines a square with size instance"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        try:
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            pass

    def area(self):
        if type(self.__size) is int:
            return (self.__size * self.__size)
        else:
            raise TypeError("size must be an integer")
