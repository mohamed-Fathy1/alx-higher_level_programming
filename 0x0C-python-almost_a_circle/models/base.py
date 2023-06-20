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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__) + ".json"
        content_text = []
        if list_objs:
            for item in list_objs:
                content_text.append(item.to_dictionary())
            content_text = Base.to_json_string(content_text)
        else:
            content_text = "[]"
        with open(filename, 'w+', encoding='utf-8') as fd:
            fd.write(content_text)
