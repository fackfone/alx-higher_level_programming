#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is not str:
            print("{:d}".format(value))
        return True
    except ValueError or TypeError:
        return False
    else:
        return False