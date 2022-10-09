from math import *

def bissection(function, a, b, n):
    """Returns a root in the interval [a,b] of a function f, given a certain error"""
    guess = (a + b) / 2  # initial guess in the middle of the interval
    it = 0  # iteration counter
    print('It {}: a = {}; b = {}, x = {}, f(x) = {}'.format(it, a, b, guess, function(guess)))

    while it < n:  # stop condition
        it += 1
        if function(guess) > 0 and function(a) > 0 or function(guess) < 0 and function(a) < 0:
            a = guess  # setting the new interval of bissection
        else:
            b = guess
        guess = (a + b) / 2  # next guess, after a or b are changed
        print('It {}: a = {}; b = {}, x = {}, f(x) = {}'.format(it, a, b, guess, function(guess)))

    return guess


def f(x):
    return sqrt(x) - cos(x)

bissection(f, 0, 1, 4)
