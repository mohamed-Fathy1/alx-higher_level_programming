#!/usr/bin/python3
'''module'''


def write_file(filename="", text=""):
    '''write_file function'''
    with open(filename, 'w', encoding='utf-8') as fd:
        return fd.write(text)
