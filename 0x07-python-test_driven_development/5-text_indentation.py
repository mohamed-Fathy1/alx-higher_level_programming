#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """Function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    skip = 0
    for i in text:
        if (i == " ") and (skip == 1):
            continue;
        skip = 0
        print(i, end="")
        if i in ('.', '?', ':'):
            skip = 1
            print("\n")
