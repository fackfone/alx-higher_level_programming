#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    string = ""
    for element in my_string:
        if element != 'c' and element != 'C':
            string += element
    return string
