#!/usr/bin/python3
'''4-inherits_from.py module'''


def inherits_from(obj, a_class):
    '''inherits_from function'''
    return issubclass(type(obj), a_class) and \
        not type(obj).__name__ == a_class.__name__
