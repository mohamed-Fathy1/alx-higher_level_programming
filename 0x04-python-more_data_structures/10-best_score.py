#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return (sorted(a_dictionary.items())[len(a_dictionary) - 1][0])
    return (None)
