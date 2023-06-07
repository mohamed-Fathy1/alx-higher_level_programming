#!/usr/bin/python3
''' Rectangle module'''


class Rectangle:
    '''Rectangle class'''
    def __init__(self, width=0, height=0) -> None:
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError('width must be >= 0')
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if 0 in (self.__height, self.__width):
            return (0)
        return (2 * (self.__height + self.__width))
