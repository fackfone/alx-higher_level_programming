#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    k = 0
    while (k < len(matrix)):
        for i in matrix[k]:
            print("{:d}".format(i), end=" ")
        print("")
        k += 1
