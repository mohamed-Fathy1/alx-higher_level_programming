#!/usr/bin/python3
'''Write a function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    '''Find a peak in a list of unsorted integers.'''
    start, end = 0, len(list_of_integers) - 1
    while (start <= end):
        mid = start + ((end - start) // 2)
        if ((mid < len(list_of_integers) - 1)
                and (list_of_integers[mid + 1] > list_of_integers[mid])):
            start = mid + 1
        elif (mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]):
            end = mid - 1
        else:
            return (list_of_integers[mid])
