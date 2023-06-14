#!/usr/bin/python3
'''module'''
import json


def load_from_json_file(filename):
    '''load_from_json_file'''
    with open(filename, 'r') as fd:
        return json.loads(fd.read())
