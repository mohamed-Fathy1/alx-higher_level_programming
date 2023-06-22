#!/usr/bin/python3
''' Base Module'''
import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        '''from_json_string method'''
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        if str(cls.__name__) == "Rectangle":
            dummy_object = cls(4, 4)
        else:
            dummy_object = cls(4)

        dummy_object.update(**dictionary)
        return dummy_object

    @classmethod
    def load_from_file(cls):
        '''load_from_file function'''
        filename = str(cls.__name__) + ".json"
        instances = []
        try:
            with open(filename, 'r') as fd:
                json_text = Base.from_json_string(fd.read())

            for obj in json_text:
                instances.append(cls.create(**obj))
            return instances
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as fd:
            if filename == 'Rectangle.csv':
                filefelids = ['id', 'width', 'height', 'x', 'y']
            else:
                filefelids = ['id', 'size', 'x', 'y']
            csv_writer = csv.DictWriter(fd, fieldnames=filefelids)
            if list_objs:
                file_objs = [item.to_dictionary() for item in list_objs]
            else:
                file_objs = '[]'
            for line in file_objs:
                csv_writer.writerow(line)

    @classmethod
    def load_from_file_csv(cls):
        '''load_from_file function'''
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, 'r') as fd:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                csv_reader = csv.DictReader(fd, fieldnames=fieldnames)
                csv_reader = [dict([k, int(v)] for k, v in d.items())
                              for d in csv_reader]
                for obj in csv_reader:
                    instances.append(cls.create(**obj))
            return instances
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''draw shapes'''
        shape_list = list_rectangles + list_squares
        draw_shape = turtle.Turtle()
        draw_shape.title('Screen Demo')
        draw_shape.bgcolor('yellow')
        draw_shape.exitonclick()
