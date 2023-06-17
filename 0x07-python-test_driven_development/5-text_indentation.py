#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """Function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        print(i, end="")
        if i in ('.', '?', ':'):
            print("\n")
