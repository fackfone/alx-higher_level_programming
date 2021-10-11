#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class Rectangle which inherits
from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Class Rectangle"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
