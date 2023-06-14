#!/usr/bin/python3
'''module'''


def append_after(filename="", search_string="", new_string=""):
    '''append_after function'''
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
