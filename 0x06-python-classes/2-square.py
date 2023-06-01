#!/usr/bin/python3
"""class Square."""


class Square:
    """quare iner class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        else if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
