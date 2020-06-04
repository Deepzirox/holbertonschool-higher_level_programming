#!/usr/bin/python3
import json
"""[summary]
"""

def load_from_json_file(filename):
    """[summary]

    Args:
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(filename, "r") as file:
        return json.loads(file)