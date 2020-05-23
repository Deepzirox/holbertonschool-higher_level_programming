#!/usr/bin/python3
"""[3-say_my_name]
"""


def say_my_name(first_name, last_name=""):
    """[say_my_name]
    Arguments:
        first_name {[str]}

    Keyword Arguments:
        last_name {str}

    Raises:
        TypeError: [first_name must be a string]
        TypeError: [last_name must be a string]
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
