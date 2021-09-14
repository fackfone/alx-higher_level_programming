#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return

    integerList = reversed(my_list)
    for i in integerList:
        print("{:d}".format(i))
