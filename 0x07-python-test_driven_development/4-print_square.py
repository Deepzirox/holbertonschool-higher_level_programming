#!/usr/bin/python3
"""[4-print_square]
"""


def print_square(size):
    """[print_square]

    Arguments:
        size {[type]} -- [size of square]

    Raises:
        TypeError: [size must be an integer]
        TypeError: [size must be an integer]
        ValueError: [size must be >= 0]
    """
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    if type(size) in [float] and size <= 0.9:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for s in range(int(size)):
        print('#' * int(size))
