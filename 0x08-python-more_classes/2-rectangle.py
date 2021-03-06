#!/usr/bin/python3
""" defines a rectangle"""


class Rectangle:
    """Empty class Rectangle"""

    def __init__(self, width=0, height=0):
        """ intializer
        Args
           width
           height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width"""
        return self.__width

    @property
    def height(self):
        """gets height"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets width
        Args:
        value: width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height
        Args:
        value: height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """computes area"""
        result = self.width * self.height
        return(result)

    def perimeter(self):
        """computes perimeter"""
        if self.width == 0 or self.height == 0:
            result = 0
            return(result)
        result = (self.width * 2) + (self.height * 2)
        return(result)
