import numpy as np
import numpy.linalg as lin
from sympy import false, true
import A_Matrix_in_D_L_R_unterteilen


def gauss_seidel(prev_x):
    return -lin.inv(D + L).dot(R).dot(prev_x) + lin.inv(D + L).dot(b)

def gauss_seidel_vergleiche_toleranz(prev_value, next_value):
    for i in range(len(prev_value)):
        if (np.abs(prev_value[i] - next_value[i]) > toleranz):
            return false
    return true
    
def gauss_seidel_mit_toleranz(startvektor):
    previous_value = startvektor
    next_x_value = np.full(len(previous_value), -100)
    iteration_count = 0

    while (not gauss_seidel_vergleiche_toleranz(previous_value, next_x_value)):
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            previous_value = next_x_value
        next_x_value = gauss_seidel(previous_value)
        print(f"x^{iteration_count} = {previous_value} -> {next_x_value}")
        iteration_count = iteration_count + 1
    print("Fixpunkt: ", next_x_value)
    # Gebe Fixpunkt zurück
    return next_x_value
    


def gauss_seidel_mit_anzahl_iterationen(startvektor, anzahl_iterationen):
    previous_value = startvektor
    next_x_value = -100

    for i in range(anzahl_iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value
        next_x_value = gauss_seidel(previous_value)
        print(f"x^{i} = {previous_value} -> {next_x_value}")

# Variablen definieren
toleranz = 10**-4
startvektor = np.array([1, -1, 3])
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])
[L, R, D] = A_Matrix_in_D_L_R_unterteilen.unterteilen(A)

# Fixpunkt mit Toleranz berechnen
# fixpunkt = gauss_seidel_mit_toleranz(startvektor)
# Fixpunkt mit Anzahl Iterationsschritten berechnen
gauss_seidel_mit_anzahl_iterationen(startvektor, 4)