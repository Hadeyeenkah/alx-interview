#!/usr/bin/python3
"""
0. Rotate 2D Matrix
This module contains a function to rotate a given n x n 2D matrix
90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The 2D matrix to rotate.

    Returns:
        None: The matrix is rotated in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    c, r = 0, rows - 1

    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])
        if r == -1:
            r = rows - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cols - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
