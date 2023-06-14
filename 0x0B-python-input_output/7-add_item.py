#!/usr/bin/python3
'''module main'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
from_json_string = __import__('4-from_json_string').from_json_string


if __name__ == '__main__':
    my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])

    save_to_json_file(my_list, "add_item.json")
    with open("add_item.json", )
    from_json_string()
