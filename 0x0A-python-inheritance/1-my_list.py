#!/usr/bin/python3
''' my_list module '''


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        ''' print_sorted function'''
        print(sorted(self))
