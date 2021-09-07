#!/usr/bin/python3
for a in range(10):
    for b in range(a, 10):
        if a != b and (a != 8 or b != 9):
            print("{}{}, ".format(a, b), end="")
        elif a == 8 and b == 9:
            print("{}{}".format(a, b))
