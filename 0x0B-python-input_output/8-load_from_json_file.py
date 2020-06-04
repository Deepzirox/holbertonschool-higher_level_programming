#!/usr/bin/python3
"""[summary]
"""

import json


def load_from_json_file(filename):
    """[summary]

    Args:
        filename ([type]): [description]

    Returns:
        [type]: [description]
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.loads(file)