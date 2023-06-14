#!/usr/bin/python3
'''module'''


def append_write(filename="", text=""):
    '''write_file function'''
    with open(filename, 'a', encoding='utf-8') as fd:
        return fd.write(text)
