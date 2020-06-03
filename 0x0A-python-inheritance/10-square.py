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
        """[summary]

        Raises:
            Exception: [description]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[summary]

        Arguments:
            name {[type]} -- [description]
            value {[type]} -- [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """[summary]

    Arguments:
        BaseGeometry {[type]} -- [description]
    """
    def __init__(self, width, height):
        super().integer_validator
        super().area
        self.__width = width
        self.__height = height
        self.integer_validator(str(height), self.__height)
        self.integer_validator(str(width), self.__width)

    def area(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return self.__width * self.__height

    def __str__(self):
        """[summary]

        Returns:
            [type] -- [description]
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """[summary]

    Arguments:
        Rectangle {[type]} -- [description]
    """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
        #self.integer_validator(str(self.__size), size)
