#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    top = 0
    bottom = 0
    for score, weight in my_list:
        top += (score * weight)
        bottom += weight
    if bottom:
        result = top/bottom
    return (result)
