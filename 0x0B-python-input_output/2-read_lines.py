#!/usr/bin/python3
"""[summary]
"""


def read_lines(filename="", nb_lines=0):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        nb_lines (int, optional): [description]. Defaults to 0.
    """    
    with open(filename) as file:
        data = file.read()
        if nb_lines <= 0:
            print(data, end='')
        else:
            jumps = 0
            for i in data:
                if i == '\n':
                    print()
                    jumps += 1
                    continue
                if jumps == nb_lines:
                    break
                print(i, end='')
