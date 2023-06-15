#!/usr/bin/python3
'''module'''


class MyInt(int):
    '''MyInt class'''

    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
