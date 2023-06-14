
#!/usr/bin/python3
"""Student module"""


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_list = {}
            for i in self.__dict__:
                for j in attrs:
                    if i == j:
                        new_list[i] = self.__dict__[i]
            return new_list
        return self.__dict__
