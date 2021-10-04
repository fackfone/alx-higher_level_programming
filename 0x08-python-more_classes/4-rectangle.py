#!/usr/bin/python3
"""
This module defines a class
Rectangle with width and height
It also allows the caluclation
of area and perimeter
"""


class Rectangle:
    """
    Creates a class that defines a rectangle with
    defining the way to calculate area and perimeter
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def __str__(self):
        s = ""
        if self.__width == 0 or self.__height == 0:
            return s
        for i in range(self.__height):
            for j in range(self.__width):
                s += "#"
            if i != (self.__height - 1):
                s += '\n'
        return s

    def __repr__(self):
        s2 = "Rectangle(" + str(self.__width) + ", " + str(self.__height)+")"
        return s2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
