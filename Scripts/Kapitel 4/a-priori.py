import numpy as np
import numpy.linalg as lin
from sympy import false
# import A_Matrix_in_D_L_R_unterteilen

toleranz = 10**(-4)
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])
debug = false

# Jacobi
# Funktion einfügen
# [L, R, D] = A_Matrix_in_D_L_R_unterteilen.unterteilen(A)
D = np.diag(np.diag(A))
R = np.triu(A) - D
L = np.tril(A) - D

B = -lin.inv(D).dot(L+R)
B_norm = lin.norm(B, np.inf)


if debug:
    print(f"||x^(n) - x̄||∞ ≤ ((||B||∞)^n / (1-||B||∞)) * ||x^(1) - x^(0)||∞ ≤ {toleranz}")

print(f"{B_norm}")