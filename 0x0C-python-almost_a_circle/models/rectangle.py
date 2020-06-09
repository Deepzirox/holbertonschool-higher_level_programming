#!/usr/bin/python3
"""[Rectangle.py]
"""
from models.base import Base


class Rectangle(Base):
    """[Clase Rectangle]

    Args:
        Base ([Class]): [Base class]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """[summary]

        Args:
            width ([type]): [description]
            height ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.

        Raises:
            TypeError: [description]
            ValueError: [description]
            TypeError: [description]
            ValueError: [description]
            TypeError: [description]
            ValueError: [description]
            TypeError: [description]
            ValueError: [description]
        """
        super().__init__(id)
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) not in [int]:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) not in [int]:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__width

    @width.setter
    def width(self, width):
        """[summary]

        Args:
            width ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__height

    @height.setter
    def height(self, height):
        """[summary]

        Args:
            height ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__x

    @x.setter
    def x(self, x):
        """[summary]

        Args:
            x ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(x) not in [int]:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.__y

    @y.setter
    def y(self, y):
        """[summary]

        Args:
            y ([type]): [description]

        Raises:
            TypeError: [description]
            ValueError: [description]
        """
        if type(y) not in [int]:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.width * self.height

    def display(self):
        """[summary]
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        values = "({}) {}/{} - ".format(self.id, self.x, self.y)
        values += "{}/{}".format(self.width, self.height)
        return "[Rectangle] {}".format(values)

    def update(self, *args, **kwargs):
        """[summary]
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        else:
            for ag in range(len(args)):
                if ag == 0:
                    self.id = args[ag]
                elif ag == 1:
                    self.width = args[ag]
                elif ag == 2:
                    self.height = args[ag]
                elif ag == 3:
                    self.x = args[ag]
                elif ag == 4:
                    self.y = args[ag]

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
