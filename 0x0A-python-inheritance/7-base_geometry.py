#!/usr/bin/python3
'''module'''


class BaseGeometry():
    '''BaseGeometry class'''
    def area(self):
        '''area'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''integer_validator method'''
        if value.__class__ !=  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
