#!/usr/bin/python3
def islower(c):
    i = 97
    while(i < 123):
        if(ord(c) == i):
            return True
        i += 1


def uppercase(str):
    for j in str:
        if(islower(j)):
            j = chr(ord(j) - 32)
        print("{}".format(j), end="")
    print("")
