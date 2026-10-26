# Project Penguin
# Chapter: Chaos
# Date: 26-10-2026
#
# Plot the logistic map

import numpy as np

# Create a logistic functions, should work on floats as well
def logistic(x, r):
    return r * x * (1 - x)

# Return [x0, f(x0), f(f(x0)), ...] with n iterates after x0.
# Note that this is 1D.
def orbit(f, x0, n):
    # Pre-allocate the array as empty
    xs = np.empty(n + 1)
    xs[0] = x0
    for i in range(n):
        xs[i + 1] = f(xs[i])
    return xs

# should settle near 1 - 1/2.8 ≈ 0.643
orbit(lambda x: logistic(x, 2.8), 0.2, 30)[-5:]
# alternates between two values
orbit(lambda x: logistic(x, 3.2), 0.2, 30)[-4:]

r = np.array([2.8, 3.2, 3.9])
logistic(0.5, r)
