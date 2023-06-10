#!/usr/bin/python3
"""module"""


def text_indentation(text):
    """Function"""
    if type(text) is not str:
        raise TypeError('text must be a string')

    j = 0
    deli = '.?:'

    for i, char in enumerate(text):
        for delim in deli:
            if char is delim:
                j += 1
                text = text[:i + j] + ' ' + text[i + j:]

    list = text.split()

    for ele in list:
        if ele[-1:] is "." or ele[-1:] is "?" or ele[-1:] is ":":
            print(ele, end="\n\n")
        elif ele is list[len(list) - 1]:
            print(ele, end="")
        else:
            print(ele, end=" ")
