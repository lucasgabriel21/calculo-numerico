from math import *

def f(x):
    return sin(7*x) - 0.4*x


def secant_root(f, x0, x1, it):
    iteration = 0
    print('It {}: x = {} and f(x) = {}'.format(iteration, x0, f(x0)))
    iteration += 1
    print('It {}: x = {} and f(x) = {}'.format(iteration, x1, f(x1)))
    iteration += 1

    for i in range(it-1):
        try:
            x2 = x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
            x0 = x1
            x1 = x2
            print('It {}: x = {} and f(x) = {}'.format(iteration, x1, f(x1)))

            if f(x1) == 0:
                print('Best aproximation found at iteration {}'.format(iteration))
                break

            iteration += 1

        except ZeroDivisionError:
            print('Best aproximation found at iteration {}'.format(iteration-1))
            break

secant_root(f, 0.4, 0.5, 12)