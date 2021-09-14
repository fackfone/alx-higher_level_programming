#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for listInt in matrix:
        for integer in listInt:
            print('{:d}'.format(integer), end='')
            if integer != listInt[-1]:
                print(' ', end='')
        print("")
