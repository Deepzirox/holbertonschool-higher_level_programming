#!/usr/bin/python3


#!/usr/bin/python3
"""[summary]

    Raises:
        Exception: [description]
        TypeError: [description]
        ValueError: [description]
"""

class BaseGeometry:
    """[summary]
    """    
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)
