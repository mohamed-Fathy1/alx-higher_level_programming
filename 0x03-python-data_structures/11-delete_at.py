#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        for index, i in enumerate(my_list):
            if index == idx:
                del my_list[index]
    return (my_list)
