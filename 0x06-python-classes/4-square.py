#!/usr/bin/python3
class Square:
    """A class that defines a square with size instance"""
    def __init__(self, size=0, position=(0, 0)):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
            self.__size = value

    def area(self):
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        return (self.__size * self.__size)
