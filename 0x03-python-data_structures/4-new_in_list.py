#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if (my_list == []):
        return None
    for integer in my_list:
        new_list.append(integer)
    if (idx < 0 or idx > len(my_list) - 1):
        return my_list
    else:
        new_list[idx] = element
        return new_list
