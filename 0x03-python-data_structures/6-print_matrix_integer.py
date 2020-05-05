#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        h = len(row)
        c = 0
        for col in row:
            print(col, end='')
            if c != h - 1:
                print(' ', end='')
            c += 1
        print('')
