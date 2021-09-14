#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_number = my_list[0]
    for i in range(len(my_list) - 1):
        if max_number > my_list[i + 1]:
            pass
        else:
            max_number = my_list[i + 1]
    return max_number
