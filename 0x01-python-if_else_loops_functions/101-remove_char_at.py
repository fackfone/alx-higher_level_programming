#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0:
        str = str[1:]
    elif n == -1:
        str = str[:-2]
    elif(n > 0 or n < 0):
        str = str[:n] + str[n + 1:]
    elif n > len(str):
        pass
    return str
