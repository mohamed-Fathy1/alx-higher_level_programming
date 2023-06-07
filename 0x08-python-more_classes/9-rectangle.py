#!/usr/bin/python3
''' Rectangle module'''


class Rectangle:
    '''Rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        if 0 in (self.__height, self.__width):
            return ("")
        val = []
        for i in range(self.__height):
            [val.append(str(self.print_symbol)) for j in range(self.__width)]
            val.append('\n') if i is not self.__height - 1 else ""
        return ("".join(val))

    def __repr__(self) -> str:
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
