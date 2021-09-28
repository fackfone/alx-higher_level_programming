#!/usr/bin/python3
"""Defines a Square class that defines a square
object with private attributes, handle getter and
setter, and exceptions (ValueError and TypeError).
Prints in stdout the square with the character #"""


class Square:
    """A class that defines a square with size instance"""
    def __init__(self, size=0):
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

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
