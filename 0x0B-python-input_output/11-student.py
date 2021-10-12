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

    def to_json(self, attrs=None):
        """
        Retreves a dictionary representation of a
        Student instance
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

    def reload_from_json(self, json):
        """
        This function replaces all attributes of the Student instance
        """
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
