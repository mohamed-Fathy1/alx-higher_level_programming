#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if 0 <= idx < len(my_list):
        for index, i in enumerate(my_list):
            if index == idx:
                new_list.append(element)
            else:
                new_list.append(i)
        return (new_list)
    return (my_list)
