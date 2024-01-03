import A_Matrix_in_D_L_R_unterteilen
import numpy as np
import numpy.linalg as lin
from sympy import false, true


def gauss_seidel(prev_x, debug=False):
    if debug:
        print(
            f"-> \n{-lin.inv(D + L).dot(R)}\n * \n{prev_x.reshape(-1, 1)}\n + \n{(lin.inv(D + L).dot(b)).reshape(-1, 1)}\n"
        )
    return -lin.inv(D + L).dot(R).dot(prev_x) + lin.inv(D + L).dot(b)


def print_gauss_seidel_zwischenschritte():
    print("---------------------------------------")
    print("x^k+1 = -inv(D + L) * R * x^0 + inv(D + L) * b \n")
    print(
        f"= -inv(\n{D + L}\n) * \n{R}\n * x_k + inv(\n{D + L}\n) * \n{b.reshape(-1, 1)}\n"
    )
    print("Vereinfacht: ")
    print(
        f"= \n{-lin.inv(D + L)}\n * \n{R}\n * x_k + \n{lin.inv(D + L)}\n * \n{b.reshape(-1, 1)}\n"
    )
    print("Vereinfacht: ")
    print(
        f"= \n{-lin.inv(D + L).dot(R)}\n * x_k + \n{(lin.inv(D + L).dot(b)).reshape(-1, 1)}\n"
    )


def gauss_seidel_vergleiche_toleranz(prev_value, next_value):
    for i in range(len(prev_value)):
        if np.abs(prev_value[i] - next_value[i]) > toleranz:
            return false
    return true


def gauss_seidel_mit_toleranz(startvektor, debug=False):
    previous_value = startvektor
    next_x_value = np.full(len(previous_value), -100)
    iteration_count = 0

    if debug:
        print_gauss_seidel_zwischenschritte()

    while not gauss_seidel_vergleiche_toleranz(previous_value, next_x_value):
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            previous_value = next_x_value
        if debug:
            print(f"Gauss-Seidel Iteration: {iteration_count + 1}")
            print(f"x^{iteration_count} = \n{previous_value.reshape(-1, 1)}")
        next_x_value = gauss_seidel(previous_value, debug)
        print(f"= \n{next_x_value.reshape(-1, 1)}")
        print("--------------")
    print("Fixpunkt: ", next_x_value)
    # Gebe Fixpunkt zurück
    return next_x_value


def gauss_seidel_mit_anzahl_iterationen(startvektor, anzahl_iterationen, debug=False):
    previous_value = startvektor
    next_x_value = -100
    x_values = [previous_value]

    if debug:
        print_gauss_seidel_zwischenschritte()

    for i in range(anzahl_iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value
        if debug:
            print(f"Gauss-Seidel Iteration: {i + 1}")
            print(f"x^{i} = \n{previous_value.reshape(-1, 1)}")
        next_x_value = gauss_seidel(previous_value, debug)
        x_values.append(next_x_value)
        print(f"= \n{next_x_value.reshape(-1, 1)}")
        print("--------------")
    return x_values


# Variablen definieren
toleranz = 10**-4
startvektor = np.array([4, 3, -0.5])
A = np.array([[2, -1, 0], [-1, 4, 1], [0, 1, 2]])
b = np.array([4, 5, -2])
[L, R, D] = A_Matrix_in_D_L_R_unterteilen.unterteilen(A, True)

# Fixpunkt mit Toleranz berechnen
# fixpunkt = gauss_seidel_mit_toleranz(startvektor)
# Fixpunkt mit Anzahl Iterationsschritten berechnen
gauss_seidel_mit_anzahl_iterationen(startvektor, 1, True)
