#!/usr/bin/python
def no_c(my_string):
    str_list = []
    string = ""
    for char in my_string:
        str_list.append(char)
    if 'c' in str_list:
        str_list.remove("c")
    if 'C' in str_list:
        str_list.remove("C")
    for element in str_list:
        string += element
    return string
