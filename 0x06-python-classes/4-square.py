#!/usr/bin/python3
class Square:
    """A class that defines a square with size instance"""

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

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        if type(self.__size) is int:
            return (self.__size * self.__size)
        else:
            raise TypeError("size must be an integer")
