#!/usr/bin/python3
"""Module built divide"""


def matrix_divided(matrix, div):
    """Function divides"""
    matrix_copy = []

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
            tmp.append(round(j / div, 2))
        matrix_copy.append(tmp)
    return matrix_copy
