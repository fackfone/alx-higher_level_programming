#!/usr/bin/python3
def magic_string():
    s1, s2 = "Best School","Best School"
    if (s2 == s1): 
        return s1
    s1 = s1 + "," + s2
    return (s1 + ", " + s2)

