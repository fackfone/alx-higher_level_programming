#!/usr/bin/python3
def matrix_divided(matrix, div):
    err = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    if not isinstance(matrix, list):
        raise TypeError(err)
    if matrix is None:
        raise TypeError(err)
    if len(matrix) >= 2:
        checker = matrix[0]
        for element in matrix:
            if int((len(checker))) != int(len(element)):
                raise TypeError(err2)
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0 or div == div + 1:
        raise ZeroDivisionError("division by zero")
    divided = [[round(row[i] / float(div), 2)
                for i in range(len(matrix[0]))] for row in matrix]
    return divided
