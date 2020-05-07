#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    sup = []
    for rows in matrix:
        for col in rows:
            sup.append(col * col)
        else:
            new.append(sup)
            sup = []
    return new
