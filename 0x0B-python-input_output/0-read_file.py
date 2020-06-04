#!/usr/bin/python3
"""[0-read_file]
"""


def read_file(filename=""):
    """[summary]

    Args:
        filename (str, optional): [Path of file]. Defaults to "".
    """
    with open(filename) as file:
        print(file.read())
