import A_Matrix_in_D_L_R_unterteilen
import numpy as np
import numpy.linalg as lin
from sympy import false, true


def jacobi(prev_x, debug=False):
    if debug:
        print(
            f"-> \n{-lin.inv(D).dot(L + R)}\n * \n{prev_x.reshape(-1, 1)}\n + \n{(lin.inv(D).dot(b)).reshape(-1, 1)}\n"
        )
    return -lin.inv(D).dot(L + R).dot(prev_x) + lin.inv(D).dot(b)


def print_jacobi_zwischenschritte():
    print("---------------------------------------")
    print("x^k+1 = -inv(D) * (L + R) * x^0 + inv(D) * b \n")
    print(
        f"= -inv(\n{D}\n) * \n{L + R}\n * x_k + inv(\n{D}\n) * \n{b.reshape(-1, 1)}\n"
    )
    print("Vereinfacht: ")
    print(
        f"= \n{-lin.inv(D)}\n * \n{L + R}\n * x_k + \n{lin.inv(D)}\n * \n{b.reshape(-1, 1)}\n"
    )
    print("Vereinfacht: ")
    print(
        f"= \n{-lin.inv(D).dot(L + R)}\n * x_k + \n{(lin.inv(D).dot(b)).reshape(-1, 1)}\n"
    )


def vergleiche_toleranz(prev_value, next_value):
    for i in range(len(prev_value)):
        if np.abs(prev_value[i] - next_value[i]) > toleranz:
            return false
    return true


def jacobi_mit_toleranz(startvektor, debug=False):
    previous_value = startvektor
    next_x_value = np.full(len(previous_value), -100)
    iteration_count = 0

    if debug:
        print_jacobi_zwischenschritte()

    while not vergleiche_toleranz(previous_value, next_x_value):
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            previous_value = next_x_value
        if debug:
            print(f"Jacobi Iteration: {iteration_count + 1}")
            print(f"x^{iteration_count} = \n{previous_value.reshape(-1, 1)}")
        next_x_value = jacobi(previous_value, debug)
        print(f"= \n{next_x_value.reshape(-1, 1)}")
        iteration_count = iteration_count + 1
    # Gebe Fixpunkt zurück
    return next_x_value


def jacobi_mit_anzahl_iterationen(startvektor, anzahl_iterationen, debug=False):
    previous_value = startvektor
    next_x_value = -100
    x_values = [previous_value]

    if debug:
        print_jacobi_zwischenschritte()

    for i in range(anzahl_iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value
        if debug:
            print(f"Jacobi Iteration: {i + 1}")
            print(f"x^{i} = \n{previous_value.reshape(-1, 1)}")
        next_x_value = jacobi(previous_value, debug)
        x_values.append(next_x_value)
        print(f"= \n{next_x_value.reshape(-1, 1)}")
    return x_values


# Variablen definieren
# startvektor = np.array([4, 3, -0.5])
# A = np.array([[2, -1, 0], [-1, 4, 1], [0, 1, 2]])
# b = np.array([4, 5, -2])
A = np.array([[3, 2], [1, 3]])
b = np.array([1, 0])
startvektor = np.array([1, 1])
[L, R, D] = A_Matrix_in_D_L_R_unterteilen.unterteilen(A, True)
# Toleranz definieren
toleranz = 10**-4


# Fixpunkt mit Toleranz berechnen
# fixpunkt = jacobi_mit_toleranz(startvektor)
jacobi_mit_anzahl_iterationen(startvektor, 1, True)
# print("Fixpunkt: ", fixpunkt)
