#!/usr/bin/python3
"""reinas puzzle
"""
import sys


def validate_new_queen(reinas, new_queen):
    """Check array new_queen
    """
    for row, y in reinas:
        if y == new_queen[1]:
            return False
        if abs((y - new_queen[1]) / (row - new_queen[0])) == 1:
            return False
    return True


def generate_places(n, reinas, solutions):
    """set place of new_queen
    """
    if len(reinas) == n:
        for q in reinas:
            solutions.append(q)
        return
    row = len(reinas)
    for y in range(n):
        new_queen = [row, y]
        if validate_new_queen(reinas, new_queen):
            reinas.append(new_queen)
            generate_places(n, reinas, solutions)
            reinas.pop()


def check_argv():
    """Validate N passed
    """
    if len(sys.argv) != 2:
        print('Usage: nreinas N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    return n


def print_res(solutions, n):
    """
    print the result
    """
    final_res = []
    cont = 0
    for m in solutions:
        cont += 1
        final_res.append(m)
        if cont == n:
            cont = 0
            print(final_res)
            final_res = []


def nqueens():
    """define program main
    """
    n = check_argv()
    reinas = []
    solutions = []
    generate_places(n, reinas, solutions)
    print_res(solutions, n)


if __name__ == '__main__':
    nqueens()
