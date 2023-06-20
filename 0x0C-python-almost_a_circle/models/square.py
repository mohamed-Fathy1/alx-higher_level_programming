#!/usr/bin/python3
"""Defines square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''print object structer'''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = self.height = value

    def update(self, *args, **kwargs):
        '''update the the object'''
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        if kwargs:
            for key, val in kwargs.items():
                if key == 'id':
                    if val is None:
                        self.__init__(self.size, self.size, self.x, self.y)
                    else:
                        self.id = val
                elif key == 'size':
                    self.size = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        '''return dict'''
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
