#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    index = 0
    for c in str:
        if index != n:
            str2 += c
        index += 1
    return str2
