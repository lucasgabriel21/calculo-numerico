import numpy as np
from math import *

points = np.array([(-0.6975, 2.0840), (-0.6762, 2.0330), (0.0176, 0.8472), (0.4512, 0.6773), (0.7559, 0.4318)])
n = len(points)
# f(x) = a1 + a2*exp(-x)

# SOMATÓRIOS
sum_exp_xi = 0
sum_exp_xi_sqr = 0
sum_yi_exp_xi = 0
sum_yi = 0
for p in points:
    xi, yi = p[0], p[1]
    sum_exp_xi += exp(-xi)
    sum_exp_xi_sqr += exp(-xi)**2
    sum_yi_exp_xi += yi*exp(-xi)
    sum_yi += yi
# print(sum_exp_xi)
# print(sum_exp_xi_sqr)
# print(sum_yi_exp_xi)
# print(sum_yi)

a1 = (sum_yi_exp_xi*sum_exp_xi - sum_yi*sum_exp_xi_sqr) / (sum_exp_xi**2 - n*sum_exp_xi_sqr)
a2 = (sum_yi - a1*n) / sum_exp_xi

print(a1)
print(a2)
