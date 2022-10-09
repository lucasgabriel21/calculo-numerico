from math import *

def function(x):
    return exp(-x) - x


def iteration_function(x):
    return exp(-x)


def fixed_point(g, guess, n):
    it = 0
    print('it {}: x = {}'.format(it, guess))

    while it < n:
        it += 1
        guess = g(guess)
        print('it {}: x = {}'.format(it, guess))

    return guess


x = fixed_point(iteration_function, 0, 6)
root = pi
rel_error = abs(root - x)/root
abs_error = abs(root - x)
print('Relative error = {}'.format(rel_error))
print('Absolute error: {}'.format(abs_error))
