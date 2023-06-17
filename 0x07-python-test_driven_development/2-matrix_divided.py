#!/usr/bin/python3
"""Module built divide"""


def matrix_divided(matrix, div):
    """Function divides"""
    matrix_copy = []

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if matrix and not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    size = len(matrix[0])
    for i in matrix:
        tmp = []
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) in (int, float):
                try:
                    tmp.append(round(j / div, 2))
                except ZeroDivisionError:
                    raise ZeroDivisionError("division by zero")
            else:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
        matrix_copy.append(tmp)
    return matrix_copy
