#!/usr/bin/python3
"""[summary]
"""

def write_file(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    with open(filename, mode="w+", encoding="utf-8") as file:
        file.write(text)
        return len(text)
    file.close()
