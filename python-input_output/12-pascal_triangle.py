#!/usr/bin/python3
"""
 returns a list of lists of integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_line = triangle[i-1]
        new_line = [1]
        for j in range(1, i):
            new_line.append(prev_line[j-1] + prev_line[j])
        new_line.append(1)
        triangle.append(new_line)

    return triangle
