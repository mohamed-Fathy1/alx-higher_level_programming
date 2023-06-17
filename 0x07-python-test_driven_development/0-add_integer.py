#!/usr/bin/python3
'''this is the add module'''


def add_integer(a, b=98):
    '''add_integer function'''
    if not isinstance(a, int):
        try:
            a = int(a)
        except Exception:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        try:
            b = int(b)
        except Exception:
            raise TypeError("b must be an integer")
    return (a + b)
