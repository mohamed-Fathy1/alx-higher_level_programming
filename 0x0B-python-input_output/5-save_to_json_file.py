#!/usr/bin/python3
'''module'''
import json


def save_to_json_file(my_obj, filename):
    '''write_file function'''
    with open(filename, 'w') as fd:
        return fd.write(json.dumps(my_obj))
