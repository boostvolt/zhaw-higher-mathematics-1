import numpy.linalg as l
import numpy as np

A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])
x_0 = np.array([1, -1, 3])
tol = 10 ** (-4)


def aufgabe_3_a(A, b, x_0, tol, opt="jacobi"):
    x_initial = np.copy(x_0)
    diagonal = np.diag(np.diag(A))
    upper = np.triu(A) - diagonal
    lower = np.tril(A) - diagonal
    iterations = 1

    method = jacobi if opt == "jacobi" else gauss_seidel
    result = method(diagonal, upper, lower, x_0, b)
    while l.norm(result - x_0, np.inf) > tol:
        iterations += 1
        x_0 = result
        result = method(diagonal, upper, lower, x_0, b)

    return (
        x_0,
        iterations,
        a_priori(diagonal, upper, lower, method, tol, x_initial, b),
    )


def b_jacobi(diagonal, upper, lower):
    return -l.inv(diagonal).dot(upper + lower)


def jacobi(diagonal, upper, lower, x_0, b):
    return b_jacobi(diagonal, upper, lower).dot(x_0) + l.inv(diagonal).dot(b)


def b_gauss_seidel(diagonal, upper, lower):
    return -l.inv(diagonal + lower).dot(upper)


def gauss_seidel(diagonal, upper, lower, x_0, b):
    return b_gauss_seidel(diagonal, upper, lower).dot(x_0) + l.inv(
        diagonal + lower
    ).dot(b)


def a_priori(diagonal, upper, lower, method, tol, x_0, b):
    B = l.norm(globals()["b_" + method.__name__](diagonal, upper, lower), np.inf)

    n_2 = 0
    while (B**n_2 / (1 - B)) * l.norm(
        method(diagonal, upper, lower, x_0, b) - x_0, np.inf
    ) > tol:
        n_2 += 1

    return n_2


print(aufgabe_3_a(A, b, x_0, tol, "zv"))
# TODO: Add Gauss-Seidel demo
