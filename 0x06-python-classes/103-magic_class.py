#!/usr/bin/python3
"""Defines magic class"""
import math


class MagicClass:
    """Magic class that makes matches bytecode"""

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """Area function that returns for magic class"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """This returns circumfrence of the magic class"""
        return (2 * math.pi) * self.__radius
