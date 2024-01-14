import A_Matrix_in_D_L_R_unterteilen
import numpy as np
import numpy.linalg as lin
from Gauss_Seidel import gauss_seidel_mit_anzahl_iterationen
from Jacobi import jacobi_mit_anzahl_iterationen
from sympy import false


# Jacobi
def jacobi_a_posteriori(debug=false):
    B = -lin.inv(D).dot(L + R)
    x_values = jacobi_mit_anzahl_iterationen(x_0, anzahl_iterationen)
    x_n = x_values[anzahl_iterationen]
    x_n_1 = x_values[anzahl_iterationen - 1]
    if debug:
        print("")
        print("A-Posteriori von Jacobi mit einzelnen Schritten")
    a_posteriori(B, x_n, x_n_1, debug)


# Gauss-Seidel a-priori
def gauss_seidel_a_posteriori(debug=false):
    B = -lin.inv(D + L).dot(R)
    x_values = gauss_seidel_mit_anzahl_iterationen(x_0, anzahl_iterationen)
    x_n = x_values[anzahl_iterationen]
    x_n_1 = x_values[anzahl_iterationen - 1]
    if debug:
        print("")
        print("A-Posteriori von Gauss-Seidel mit einzelnen Schritten")
    a_posteriori(B, x_n, x_n_1, debug)


# Allgemeines a-posterior Verfahren
def a_posteriori(B, x_n_1, x_n, debug=false):
    B_norm = lin.norm(B, np.inf)
    x_norm = lin.norm(x_n - x_n_1, np.inf)
    absoluter_Fehler = (B_norm / (1 - B_norm)) * x_norm

    if debug:
        print("||x^(n) - x̄||∞ ≤ ((||B||∞)^n / (1-||B||∞)) * ||x^(n) - x^(n-1)||∞")
        print(
            f"||x^({anzahl_iterationen}) - x̄||∞ ≤ (||B||∞ / (1-||B||∞)) * ||x^({anzahl_iterationen}) - x^({anzahl_iterationen-1})||∞"
        )
        print(
            f"||x^({anzahl_iterationen}) - x̄||∞ ≤ ({B_norm} / (1-{B_norm})) * ||{x_n} - {x_n_1}||∞"
        )
        print(
            f"||x^({anzahl_iterationen}) - x̄||∞ ≤ ({B_norm} / {1-B_norm}) * ||{x_n-x_n_1}||∞"
        )
        print(
            f"||x^({anzahl_iterationen}) - x̄||∞ ≤ ({B_norm} / {1-B_norm}) * {x_norm} = {absoluter_Fehler}"
        )

    # Anzahl Iterationen ungerundet zurückgeben
    print(
        f"Absoluter Fehler für a-posteriori Abschätzung für x^{anzahl_iterationen} beträgt {absoluter_Fehler}"
    )
    return absoluter_Fehler


# Variablen definieren
x_0 = np.array([1, -1, 3])
anzahl_iterationen = 3
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])
[L, R, D] = A_Matrix_in_D_L_R_unterteilen.unterteilen(A)

# Jacobi mit Debug Mode
# jacobi_a_posteriori(True)
# Jacobi ohne Debug Mode
# jacobi_a_priori(false)
# Gauss-Seidel mit Debug Mode
# gauss_seidel_a_posteriori(True)
# Gauss-Seidel ohne Debug Mode
# gauss_seidel_a_priori(false)
