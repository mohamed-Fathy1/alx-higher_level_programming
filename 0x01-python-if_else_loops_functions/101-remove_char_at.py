#!/usr/bin/python3

def remove_char_at(str, n):
    j = 0
    str1 = ""
    for i in str:
        if j == n:
            j += 1
            continue
        str1 += i
        j += 1
    return (str1)
