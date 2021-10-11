#!/usr/bin/python3
"""
A class that returns from list
"""


class MyList(list):
    """Prints the list but sorted"""

    def print_sorted(self):

        """Prints a sorted list"""
        res = list.copy(self)
        list.sort(res)
        print(res)
