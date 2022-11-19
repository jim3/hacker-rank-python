import math
import os
import random
import re
import sys


matrix = [
    [107, 54, 128, 15],
    [12, 75, 110, 138],
    [100, 96, 34, 85],
    [75, 15, 28, 112]
]


def flippingMatrix(matrix):
    arr = []
    arrLength = len(matrix[0])//2 
    for x in range(arrLength):
        for y in range(arrLength):
            arr.append(max(matrix[x][y], matrix[x][2*arrLength-y-1],
                           matrix[2 * arrLength-x-1][y], matrix[2*arrLength-x-1][2*arrLength-y-1]))
    return sum(arr)


result = flippingMatrix(matrix)
print(result)
