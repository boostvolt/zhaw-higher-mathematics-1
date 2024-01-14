import gauss_seidel_jacobi_ldr_b_c
import numpy as np
import numpy.linalg as lin
from gauss_seidel import gauss_seidel_mit_anzahl_iterationen
from jacobi import jacobi_mit_anzahl_iterationen


# Jacobi
def jacobi_a_posteriori(A, b, x_0, iterationen, norm, debug=False):
    L, D, R = gauss_seidel_jacobi_ldr_b_c.a_in_ldr_zerlegen(A)
    B = -lin.inv(D).dot(L + R)
    x_values = jacobi_mit_anzahl_iterationen(A, b, x_0, iterationen)
    x_n = x_values[iterationen]
    x_n_1 = x_values[iterationen - 1]
    if debug:
        print("")
        print("A-Posteriori von Jacobi mit einzelnen Schritten")
    a_posteriori(B, x_n, x_n_1, iterationen, norm, debug)


# Gauss-Seidel a-priori
def gauss_seidel_a_posteriori(A, b, x_0, iterationen, norm, debug=False):
    L, D, R = gauss_seidel_jacobi_ldr_b_c.a_in_ldr_zerlegen(A)
    B = -lin.inv(D + L).dot(R)
    x_values = gauss_seidel_mit_anzahl_iterationen(A, b, x_0, iterationen)
    x_n = x_values[iterationen]
    x_n_1 = x_values[iterationen - 1]
    if debug:
        print("")
        print("A-Posteriori von Gauss-Seidel mit einzelnen Schritten")
    a_posteriori(B, x_n, x_n_1, iterationen, norm, debug)


# Allgemeines a-posterior Verfahren
def a_posteriori(B, x_n_1, x_n, iterationen, norm, debug=False):
    B_norm = lin.norm(B, norm)
    x_norm = lin.norm(x_n - x_n_1, norm)
    absoluter_Fehler = (B_norm / (1 - B_norm)) * x_norm

    if debug:
        print("||x^(n) - x̄||∞ ≤ ((||B||∞)^n / (1-||B||∞)) * ||x^(n) - x^(n-1)||∞")
        print(
            f"||x^({iterationen}) - x̄||∞ ≤ (||B||∞ / (1-||B||∞)) * ||x^({iterationen}) - x^({iterationen-1})||∞"
        )
        print(
            f"||x^({iterationen}) - x̄||∞ ≤ ({B_norm} / (1-{B_norm})) * ||{x_n} - {x_n_1}||∞"
        )
        print(
            f"||x^({iterationen}) - x̄||∞ ≤ ({B_norm} / {1-B_norm}) * ||{x_n-x_n_1}||∞"
        )
        print(
            f"||x^({iterationen}) - x̄||∞ ≤ ({B_norm} / {1-B_norm}) * {x_norm} = {absoluter_Fehler}"
        )

    # Anzahl Iterationen ungerundet zurückgeben
    print(
        f"Absoluter Fehler für a-posteriori Abschätzung für x^{iterationen} beträgt {absoluter_Fehler}"
    )
    return absoluter_Fehler


########################################################################################

# Matrix A definieren
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])

# Vektor b definieren
b = np.array([19, 5, 34])

# Startvektor x_0 definieren
x_0 = np.array([1, -1, 3])

# Anzahl Iterationen definieren
iterationen = 3

# Norm definieren (1, 2, np.inf)
norm = np.inf

# Jacobi
jacobi_a_posteriori(A, b, x_0, iterationen, norm, True)

# Gauss-Seidel
# gauss_seidel_a_posteriori(A, b, x_0, iterationen, norm, True)
