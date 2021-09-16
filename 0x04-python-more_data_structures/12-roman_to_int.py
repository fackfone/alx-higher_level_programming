#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50,
           "C": 100, "D": 500, "M": 1000}
    sum = 0
    if roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0
    roman_list = list(roman_string)
    for key in roman_list:
        if key in dic:
            sum += dic[key]
        else:
            return 0
    return sum
