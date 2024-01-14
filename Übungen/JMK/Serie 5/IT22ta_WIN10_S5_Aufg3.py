import numpy as np


def secant(f, x0, x1, tol):
    while np.abs(x0 - x1) > tol:
        x1, x0 = x1 - ((x1 - x0) / (f(x1) - f(x0))) * f(x1), x1

    return x1


print(secant(lambda x: np.e ** (x**2) + x ** (-3) - 10, -1.0, -1.2, 10 ** (-3)))
print(
    secant(
        lambda x: -(1 / 3) * np.pi * x**3 + 5 * np.pi * x**2 - 471,
        9,
        7.6582,
        10 ** (-3),
    )
)

# Beim Netwon-Verfahren muss man f noch ableiten, was je nach f sehr mühsam sein könnte.
