#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return (None)
    tmp_max = 0
    for i in my_list:
        if i > tmp_max:
            tmp_max = i
    return (tmp_max)
