#!/usr/bin/python3
"""
This module contains a class
that defines a student
"""


class Student:
    """
    This class creates a Student object with first_name,
    last_name and age
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialisation of attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retreves a dictionary representation of a
        Student instance
        """
        return self.__dict__
