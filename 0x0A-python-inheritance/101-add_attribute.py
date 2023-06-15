#!/usr/bin/python3
'''module'''


def add_attribute(obj, attr, val):
    '''add_attribute function'''
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
