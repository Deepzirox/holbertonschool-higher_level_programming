#!/usr/bin/python3
"""[summary]
"""


class MyInt(int):
    """[summary]

    Arguments:
        int {[type]} -- [description]
    """
    def __init__(self, integer):
        self.integer = integer

    def __ne__(self, num):
        return self.integer == num

    def __eq__(self, num):
        return self.integer != num
