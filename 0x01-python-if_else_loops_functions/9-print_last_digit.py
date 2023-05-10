#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(str(abs(number))[-1])
    print(last_digit, end="")
    return (last_digit)
