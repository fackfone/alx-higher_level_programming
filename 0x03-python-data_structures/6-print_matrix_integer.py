#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        return
    k = 0
    while (k < len(matrix)):
        for i in matrix[k]:
            print("{:d}".format(i), end=" ")
        print("")
        k += 1
