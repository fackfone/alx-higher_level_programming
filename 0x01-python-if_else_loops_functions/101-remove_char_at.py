#!/usr/bin/python3
def remove_char_at(str, n):
    if n == 0:
        str = str[1:]
    elif(n > 0):
        str = str[:n] + str[n + 1:]
    elif n < 0:
        str = str[:(len(str) + n)] + str[n + len(str) + 1:]
    return str
