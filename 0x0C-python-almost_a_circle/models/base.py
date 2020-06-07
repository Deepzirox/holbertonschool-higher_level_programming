#!/usr/bin/python3
"""
    Base class for the proyect
"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = None
        if id == None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
