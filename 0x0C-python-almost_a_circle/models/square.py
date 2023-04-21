#!/usr/bin/python3
"""
A Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square repesentation"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """initialization of a square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attrib = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attrib, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrib:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}
