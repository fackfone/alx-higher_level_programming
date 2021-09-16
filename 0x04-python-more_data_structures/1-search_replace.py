#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    if search not in my_list:
        return my_list
    for integer in my_list:
        if search in my_list:
            idx = my_list.index(search)
            my_list[idx] = replace
    return my_list
