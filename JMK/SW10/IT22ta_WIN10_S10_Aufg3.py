import numpy.linalg as l
import numpy as np
import matplotlib.pyplot as plt
import timeit
from IT22ta_WIN10_S6_Aufg2 import gaussian_algorithm

# Aufgabe 3 a
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

# Aufgabe 3 b
dim = 3000
A = np.diag(np.diag(np.ones((dim, dim)) * 4000)) + np.ones((dim, dim))
dum_1 = np.arange(1, int(dim / 2 + 1), dtype=np.float64).reshape((int(dim / 2), 1))
dum_2 = np.arange(int(dim / 2), 0, -1, dtype=np.float64).reshape((int(dim / 2), 1))
x = np.append(dum_1, dum_2, axis=0)
b = A @ x
x_0 = np.zeros((dim, 1))
tol = 1e-4

# Jacobi
start = timeit.default_timer()
aufgabe_3_a(A, b, x_0, tol)
end = timeit.default_timer()
print(f"Jacobi: {end - start} s")
# 142.94855400000233 s

# Gauss-Seidel
start = timeit.default_timer()
aufgabe_3_a(A, b, x_0, tol, "gauss-seidel")
end = timeit.default_timer()
print(f"Gauss-Seidel: {end - start} s")
# 83.91509779200715 s

# Gaussian
start = timeit.default_timer()
gaussian_algorithm(A, b)
end = timeit.default_timer()
print(f"Gaussian: {end - start} s")
# TODO: Fix overflow

# np.linalg.solve
start = timeit.default_timer()
np.linalg.solve(A, b)
end = timeit.default_timer()
print(f"np.linalg.solve: {end - start} s")
# 0.21959929099830333 s

# Aufgabe 3 c
plt.figure()
plt.plot(np.abs(gaussian_algorithm(A, b) - x), label="Gauss") # TODO: Fix overflow
plt.plot(np.abs(aufgabe_3_a(A, b, x_0, tol) - x), label="Jacobi")
plt.plot(np.abs(aufgabe_3_a(A, b, x_0, tol, "gauss-seidel") - x), label="Gauss-Seidel")
plt.legend()
plt.xlabel("Vector Element")
plt.ylabel("Absolute Error")
plt.title("Absolute Error for Each Vector Element")
plt.show()
