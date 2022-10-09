from math import *

def f(x):
    return x**2 - 1.16

def df(x):
    return 2*x

def newton_raphson(f, df, x0, it):
    iteration = 0
    print('It {}: x = {} and f(x) = {}'.format(iteration, x0, f(x0)))
    iteration += 1

    for i in range(it):
        x1 = x0 - (f(x0) / df(x0))
        print('It {}: x = {} and f(x) = {}'.format(iteration, x1, f(x1)))
        x0 = x1

        if f(x0) == 0:
            print('Best aproximation found at iteration {}'.format(iteration))
            break

        iteration += 1


newton_raphson(f, df, 2.78, 2)