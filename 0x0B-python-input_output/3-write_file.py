#!/usr/bin/python3
"""[summary]
"""

def write_file(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open(filename, 'w') as file:
        file.write(text)
    file.close()
