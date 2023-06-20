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
