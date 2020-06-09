#!/usr/bin/python3
"""[Rectangle.py]
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[summary]

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """[summary]

        Args:
            size ([type]): [description]
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id ([type], optional): [description]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        values = "({}) {}/{} - ".format(self.id, self.x, self.y)
        values += "{}".format(self.width)
        return "[Square] {}".format(values)

    @property
    def size(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """[summary]

        Args:
            value ([type]): [description]
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """[summary]
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value
        else:
            for ag in range(len(args)):
                if ag == 0:
                    self.id = args[ag]
                elif ag == 1:
                    self.size = args[ag]
                elif ag == 2:
                    self.x = args[ag]
                elif ag == 3:
                    self.y = args[ag]

    def to_dictionary(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
