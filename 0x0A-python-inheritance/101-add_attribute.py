#!/usr/bin/python3
"""[summary]
"""


def add_attribute(obj, name, value):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        name {[type]} -- [description]
        value {[type]} -- [description]

    Raises:
        TypeError: [description]
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
