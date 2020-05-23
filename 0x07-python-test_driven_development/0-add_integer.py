#!/usr/bin/python3
"""[0-add_integer]
"""


def add_integer(a, b=98):
    """[add_integer]

    Arguments:
        a {[int]} -- [num]

    Keyword Arguments:
        b {int} -- [num] (default: {98})

    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]

    Returns:
        [type] -- [a+b]
    """    
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
