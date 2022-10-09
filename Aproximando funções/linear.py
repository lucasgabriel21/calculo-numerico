import numpy as np
from math import *

points = np.array([(1.5, 3.6), (3.7, 4.2), (5.2, 2.2), (7.7, 8.6)])
n = len(points)
# g(x) = ax + b

# SOMATÓRIOS
sum_xi_sqr = 0
sum_xi = 0
sum_yi = 0
sum_xi_yi = 0
for p in points:
    xi, yi = p[0], p[1]
    sum_xi_sqr += xi**2
    sum_xi += xi
    sum_yi += yi
    sum_xi_yi += xi*yi


a = (n*sum_xi_yi - sum_xi*sum_yi) / (n*sum_xi_sqr - sum_xi**2)
b = (sum_yi - a*sum_xi) / n

print(b)
