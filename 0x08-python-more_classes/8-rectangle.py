#!/usr/bin/python3
"""
iThis module defines a class
Rectangle with width and height
It also allows the caluclation
of area and perimeter
"""


class Rectangle:
    """
    Creates a class that defines a rectangle with
    defining the way to calculate area and perimeter
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = '#'

    def __str__(self):
        s = ""
        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            if i != (self.__height - 1):
                s += '\n'
        return s

    def __repr__(self):
        s2 = "Rectangle(" + str(self.__width) + ", " + str(self.__height)+")"
        return s2

    @property
    def width(self):
        self.__width = width
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        self.__height = height
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye my rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        else:
            return rect_1
