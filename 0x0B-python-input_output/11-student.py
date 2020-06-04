#!/usr/bin/python3
"""[summary]
"""


class Student:
    """[summary]
    """

    def __init__(self, first_name, last_name, age):
        """[summary]

        Args:
            first_name ([type]): [description]
            last_name ([type]): [description]
            age ([type]): [description]
        """
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self):
        """retrieves a dictionary representation of a Student instance
        """
        return self.__dict__