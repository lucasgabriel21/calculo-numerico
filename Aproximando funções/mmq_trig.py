import numpy as np
from math import *

points = np.array([(2.0, 4.3), (3.5, 7.4), (5.3, 1.2), (7.4, 4.6)])
# g(x) = a*sin(x) + b*cos(x)

# SOMATÓRIOS
sum_sin_squaredx = 0
sum_cos_squaredx = 0
sum_cos_sin_x = 0
sum_y_sinx = 0
sum_y_cosx = 0
for p in points:
    xi, yi = p[0], p[1]
    sum_sin_squaredx += sin(xi)**2
    sum_cos_squaredx += cos(xi)**2
    sum_cos_sin_x += cos(xi)*sin(xi)
    sum_y_sinx += yi*sin(xi)
    sum_y_cosx += yi*cos(xi)


a = (sum_y_sinx*sum_cos_squaredx - sum_y_cosx*sum_cos_sin_x) / (sum_sin_squaredx*sum_cos_squaredx - sum_cos_sin_x**2)
b = (sum_y_cosx - a*sum_cos_sin_x) / sum_cos_squaredx
print(a)
print(b)
