#!/usr/bin/python3
"""[summary]

    Raises:
        Exception: [description]
        TypeError: [description]
        ValueError: [description]
"""

def inherits_from(obj, a_class):
    return not issubclass(a_class, type(obj))
