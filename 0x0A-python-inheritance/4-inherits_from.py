#!/usr/bin/python3
"""[summary]

    Raises:
        Exception: [description]
        TypeError: [description]
        ValueError: [description]
"""

def inherits_from(obj, a_class):
    """[summary]

    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]

    Returns:
        [type] -- [description]
    """    
    return not issubclass(a_class, type(obj))
