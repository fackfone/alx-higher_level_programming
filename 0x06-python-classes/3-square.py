#!/usr/bin/python3
class Square:
    """A class that defines a square with size instance"""
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")

    def area(self):
        return (self.__size * self.__size)
