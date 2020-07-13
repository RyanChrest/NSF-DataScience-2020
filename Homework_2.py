# area of regular n-polygon

from math import tan, pi
n = 5
s = 6.5

area = (n * s ** 2) / (4 * tan(pi / n))

print(area)

# Intersection of 2 lines given two points on each line

import numpy as np
lines = np.array([[(2, 2), (5, -1)], [(4, 2), (-1, -2)]])

def plot(array):
    x1, y1 = array[0][0], array[0][1]
    x2, y2 = array[1][0], array[1][1]
    plt.plot([x1, x2], [y1, y2])
    
def b(array):
    x1, y1 = array[0][0], array[0][1]
    x2, y2 = array[1][0], array[1][1] 
    
    return (y1 - y2) * x1 - (x1 - x2) * y1

def coeff(array):
    x1, y1 = array[0][0], array[0][1]
    x2, y2 = array[1][0], array[1][1] 
    return (y1 - y2, x2 - x1)

def solve(array):
    matrix_b = np.array([b(lines[0]), b(lines[1])])
    matrix_a = np.array([coeff(lines[0]), coeff(lines[1])])
    if np.linalg.det(matrix_a) == 0:
        print('Lines are parallel')
        return np.full((1, 2), np.nan)
    solution = np.linalg.solve(matrix_a, matrix_b)
    return solution

print('Intersection point:', solve(lines))
