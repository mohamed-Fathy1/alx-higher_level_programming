#!/usr/bin/python3
''' mudol 2-is_same_class.py'''


def is_same_class(obj, a_class):
    '''is_same_class function'''
    return type(obj).__name__ == a_class.__name__
