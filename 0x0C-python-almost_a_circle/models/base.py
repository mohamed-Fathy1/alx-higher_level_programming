#!/usr/bin/python3
''' Base Module'''
import json


class Base:
    '''Base Class'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor'''
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return str from json'''
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"
