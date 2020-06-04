#!/usr/bin/python3
"""[summary
"""


def number_of_lines(filename=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
    """
    with open(filename) as file:
        return (len(file.readlines()))
