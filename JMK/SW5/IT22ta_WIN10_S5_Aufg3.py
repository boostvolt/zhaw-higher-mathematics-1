import numpy as np


def secant(f, x0, x1, tol):
    while np.abs(x0 - x1) > tol:
        x1, x0 = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1), x1

    return x1


print(secant(lambda x: np.e ** (x**2) + x ** (-3) - 10, -1.0, -1.2, 10 ** (-3)))
