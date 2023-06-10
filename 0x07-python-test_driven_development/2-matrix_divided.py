#!/usr/bin/python3
"""Module built divide"""


def matrix_divided(matrix, div):
    """Function divides"""
    new_matrix = []

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')
    for i in matrix:
        if type(i) is not list:
            raise TypeError('matrix must be a matrix (list of lists)' +
                            ' of integers/floats')
        if len(i) is not len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for ele in i:
            if (type(ele) is not int) and (type(ele) is not float):
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')
    if (type(div) is not int) and (type(div) is not float):
        raise TypeError('div must be a number')
    elif div is 0:
        raise ZeroDivisionError('division by zero')

    for i in matrix:
        new_row = []
        for val in i:
            quot = round((val / div), 2)
            new_row.append(quot)
        new_matrix.append(new_row)
    return new_matrix
