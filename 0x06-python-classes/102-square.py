#!/usr/bin/python3
""" Defines square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if square is equal"""
        return(self.area() == other.area())

    def __lt__(self, other):
        """Defines the less than of square"""
        return(self.area() < other.area())

    def __le__(self, other):
        """Defines the less than or equal to other square"""
        return(self.area() <= other.area())

    def __ne__(self, other):
        """Defines the not equal to another suqare"""
        return(self.area() != other.area())

    def __gt__(self, other):
        """Defines the greater than another square"""
        return(self.area() > other.area())

    def __ge__(self, other):
        """Defines the greater than or equal to another square"""
        return(self.area() >= other.area())
