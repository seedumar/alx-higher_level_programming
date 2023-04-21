#!/usr/bin/python3
"""
Define a rectangle object
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle object
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
	super().__init__(id)

    def __str__(self) -> str:
        
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name:  str, value: object, greater_equal=False):

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.check_type_value('y', y, True)
        self.__y = y

    def area(self) -> int):
        return self.width * self.height

    def display(self):
        print('\n'*self.y, end='')
        for l in range(self.height):
            print(' '*self.x + '#'*self.width)

    def update(self, *args, **kwargs):

        expect = (self.id, self.width, self.height, self.x, self.y)
        if args != ():
            self.id, self.width, self.height, self.x, self.y = \
                args + expect[len(args):len(expect)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> int:

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
}
