#!/usr/bin/python3
''' Module that finds a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' Function that finds a peak in a list of unsorted integers '''
    if not list_of_integers:
        return None
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]

    i = 1
    while i < len(list_of_integers) - 1:
        prev = list_of_integers[i - 1]
        curr = list_of_integers[i]
        next = list_of_integers[i + 1]
        if i > 2 and prev >= curr and prev >= list_of_integers[i - 2]:
            return prev
        if curr >= prev and curr >= next:
            return curr
        if (i < len(list_of_integers) - 2 and next >= curr
                and next >= list_of_integers[i + 2]):
            return prev

        i += 2
