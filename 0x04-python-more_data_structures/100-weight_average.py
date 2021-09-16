#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) < 1:
        return 0
    mul = [x * y for (x, y) in my_list]
    value = [y for (x, y) in my_list]
    sum_1, sum_2 = 0, 0
    for val in mul:
        sum_1 += val
    for integer in value:
        sum_2 += integer
    average = sum_1 / sum_2
    return average
