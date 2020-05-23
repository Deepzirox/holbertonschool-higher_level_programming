#!/usr/bin/python3
"""[matrix_divided]
"""


def matrix_divided(matrix, div):
    """ Divide Matrix
    """
    new = []
    msg1 = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) not in [list]:
        raise TypeError(msg1)
    if len(matrix) == 0:
        raise TypeError(msg1)
    else:
        for row in matrix:
            if type(row) not in [list]:
                raise TypeError(msg1)
            if len(row) == 0:
                raise TypeError(msg1)
    long = len(matrix[0])
    for row in matrix:
        if long != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) not in [list]:
            raise TypeError(msg1)
        long = len(row)
    for row in matrix:
        new.append(list(c for c in row))
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for row in new:
        for col in range(len(row)):
            if type(row[col]) not in [float, int]:
                raise TypeError(msg1)
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            else:
                row[col] = round(row[col] / div, 2)
    return new
