#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            le,gth += 1
        except (ValueError, TypeError):
            x += 1
    print("")
    return length
