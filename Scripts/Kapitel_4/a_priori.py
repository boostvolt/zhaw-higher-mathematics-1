from math import ceil

import gauss_seidel_jacobi_ldr_b_c
import numpy as np
import numpy.linalg as lin
from gauss_seidel import gauss_seidel_mit_anzahl_iterationen
from jacobi import jacobi_mit_anzahl_iterationen


# Jacobi
def jacobi_a_priori(L, D, R, b, x_0, toleranz, norm, debug=False):
    B = -lin.inv(D).dot(L + R)
    x_1 = jacobi_mit_anzahl_iterationen(A, b, x_0, 2)[1]
    if debug:
        print("")
        print("A-Priori von Jacobi mit einzelnen Schritten")
    a_priori(B, x_0, x_1, toleranz, norm, debug)


# Gauss-Seidel a-priori
def gauss_seidel_a_priori(L, D, R, b, x_0, toleranz, norm, debug=False):
    B = -lin.inv(D + L).dot(R)
    x_1 = gauss_seidel_mit_anzahl_iterationen(A, b, x_0, 2)[1]
    if debug:
        print("")
        print("A-Priori von Gauss-Seidel mit einzelnen Schritten")
    a_priori(B, x_0, x_1, toleranz, norm, debug)


# Allgemeines a-priori Verfahren
def a_priori(B, x_0, x_1, toleranz, norm, debug=False):
    B_norm = lin.norm(B, norm)
    x_norm = lin.norm(x_1 - x_0, norm)
    n = np.log(((1 - B_norm) / x_norm) * toleranz) / np.log(B_norm)

    if debug:
        print(
            f"||x^(n) - x̄||∞ ≤ ((||B||∞)^n / (1-||B||∞)) * ||x^(1) - x^(0)||∞ ≤ {toleranz}"
        )
        print(
            f"||x^(n) - x̄||∞ ≤ (({B_norm})^n / (1-{B_norm})) * ||{x_1} - {x_0}||∞ ≤ {toleranz}"
        )
        print(
            f"||x^(n) - x̄||∞ ≤ (({B_norm})^n / {1-B_norm}) * ||{x_1-x_0}||∞ ≤ {toleranz}"
        )
        print(f"||x^(n) - x̄||∞ ≤ (({B_norm})^n / {1-B_norm}) * {x_norm} ≤ {toleranz}")
        print(f"=> (({B_norm})^n / {1-B_norm}) * {x_norm} ≤ {toleranz}")
        print(f"=> (({B_norm})^n  ≤ {(1-B_norm)/x_norm} * {toleranz}")
        print(f"=> n*log({B_norm})  ≤ log({(1-B_norm)/x_norm} * {toleranz})")
        print(f"=> n ≥ log({(1-B_norm)/x_norm} * {toleranz}) / log({B_norm})")
        print(f"n ≥ {n}")
        print(f"n = {ceil(n)}")

    # Anzahl Iterationen ungerundet zurückgeben
    print(f"Anzahl Iterationsschritte mit Toleranz {toleranz}: {n} bzw. {ceil(n)}")
    return n


########################################################################################

# Matrix A definieren
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])

# Vektor b definieren
b = np.array([19, 5, 34])

# Startvektor x_0 definieren
x_0 = np.array([1, -1, 3])

# Toleranz definieren
toleranz = 10 ** (-4)

# Norm definieren (1, 2, np.inf)
norm = np.inf

# Jacobi
jacobi_a_priori(
    *gauss_seidel_jacobi_ldr_b_c.a_in_ldr_zerlegen(A), b, x_0, toleranz, norm, True
)

# Gauss-Seidel
# gauss_seidel_a_priori(
#     *gauss_seidel_jacobi_ldr_b_c.a_in_ldr_zerlegen(A), b, x_0, toleranz, norm, True
# )
