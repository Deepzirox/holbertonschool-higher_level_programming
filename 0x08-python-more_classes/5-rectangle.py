#!/usr/bin/python3
"""
5-rectangle
"""


class Rectangle:
    """
    Define Rectangle
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("ValueError")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("ValueError")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        res = ""
        if self.__height == 0 or self.__width == 0:
            return res
        else:
            for h in range(self.__height):
                res += '#' * self.__width + '\n'

        res = res[:-1]
        return res

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
