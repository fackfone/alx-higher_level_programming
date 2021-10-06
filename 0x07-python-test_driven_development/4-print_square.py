#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise TypeError("size must be >= 0")
    if size is None:
        raise TypeError("size must be an integer")
    if isinstance(size, bool):
        raise TypeError("size must be an integer")
    if (size == 0):
        print("")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
