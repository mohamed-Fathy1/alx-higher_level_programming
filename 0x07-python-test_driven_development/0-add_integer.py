#!/usr/bin/python3

def add_integer(a, b=98):
    if isinstance(a, float):
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")

    if isinstance(b, float):
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    return (a + b)
