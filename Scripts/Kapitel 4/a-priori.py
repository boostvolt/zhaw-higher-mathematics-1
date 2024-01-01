from math import ceil
import numpy as np
import numpy.linalg as lin
from sympy import false
import A_Matrix_in_D_L_R_unterteilen
from Jacobi import jacobi_mit_anzahl_iterationen
from Gauss_Seidel import gauss_seidel_mit_anzahl_iterationen

# Jacobi
def jacobi_a_priori(debug=false):
    B = -lin.inv(D).dot(L+R)
    x_1 = jacobi_mit_anzahl_iterationen(x_0, 2)[1]
    a_priori(B, x_0, x_1, debug)

# Gauss-Seidel a-priori
def gauss_seidel_a_priori(x_1, debug=false):
    B = -lin.inv(D+L).dot(R)
    x_1 = gauss_seidel_mit_anzahl_iterationen(x_0, 2)[1]
    a_priori(B, x_0, x_1, debug)

# Allgemeines a-priori Verfahren
def a_priori(B, x_0, x_1, debug=false):
    B_norm = lin.norm(B, np.inf)
    x_norm = lin.norm(x_1 - x_0, np.inf)
    n = np.log(((1-B_norm) / x_norm) * toleranz) / np.log(B_norm)

    if debug:
        print("")
        print("A-Priori von Jacobi mit einzelnen Schritten")
        print(f"||x^(n) - x̄||∞ ≤ ((||B||∞)^n / (1-||B||∞)) * ||x^(1) - x^(0)||∞ ≤ {toleranz}")
        print(f"||x^(n) - x̄||∞ ≤ (({B_norm})^n / (1-{B_norm})) * ||{x_1} - {x_0}||∞ ≤ {toleranz}")
        print(f"||x^(n) - x̄||∞ ≤ (({B_norm})^n / {1-B_norm}) * ||{x_1-x_0}||∞ ≤ {toleranz}")
        print(f"||x^(n) - x̄||∞ ≤ (({B_norm})^n / {1-B_norm}) * {x_norm} ≤ {toleranz}")
        print(f"=> (({B_norm})^n / {1-B_norm}) * {x_norm} ≤ {toleranz}")
        print(f"=> (({B_norm})^n  ≤ {(1-B_norm)/x_norm} * {toleranz}")
        print(f"=> n*log({B_norm})  ≤ log({(1-B_norm)/x_norm} * {toleranz})")
        print(f"=> n ≥ log({(1-B_norm)/x_norm} * {toleranz}) / log({B_norm})")
        print(f"n ≥ {n}")
        print(f"n = {ceil(n)}")
    
    # Anzahl Iterationen ungerundet zurückgeben
    print(
        f"Anzahl Iterationsschritte mit Toleranz {toleranz}: {n} bzw. {ceil(n)}"
    )
    return n


# Variablen definieren
x_0 = np.array([1, -1, 3])
toleranz = 10**(-4)
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])
[L, R, D] = A_Matrix_in_D_L_R_unterteilen.unterteilen(A)

# Jacobi mit Debug Mode
# jacobi_a_priori(True)
# Jacobi ohne Debug Mode
# jacobi_a_priori(false)
# Gauss-Seidel mit Debug Mode
# gauss_seidel_a_priori(True)
# Gauss-Seidel ohne Debug Mode
# gauss_seidel_a_priori(false)