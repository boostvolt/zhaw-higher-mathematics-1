import numpy as np


def is_diagonaldominant(matrix, debug=False):
    rows, cols = matrix.shape

    if check_zeilendominanz(rows, debug) or check_spaltendominanz(cols, debug):
        return True

    return False


def check_zeilendominanz(rows, debug=False):
    for i in range(rows):
        diagonal = abs(matrix[i, i])
        non_diagonal_sum = np.sum(abs(matrix[i, :])) - diagonal
        if diagonal <= non_diagonal_sum:
            return False

    if debug:
        print()
        print("Zeilensummenkriterium")
        print("für alle i = 1, ...., n |a_ii| > ∑^n _j=1, j != i |a_i,j|")
        print()

    return True


def check_spaltendominanz(cols, debug=False):
    for i in range(cols):
        diagonal = abs(matrix[i, i])
        non_diagonal_sum = np.sum(abs(matrix[:, i])) - diagonal
        if diagonal <= non_diagonal_sum:
            return False

    if debug:
        print()
        print("Spaltensummenkriterium")
        print("für alle j = 1, ...., n |a_jj| > ∑^n _i=1, i != j |a_i,j|")
        print()

    return True


########################################################################################

# Matrix definieren
matrix = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])

print(f"Strikte Diagonaldominanz: {is_diagonaldominant(matrix, True)}")
print(
    "Falls A diagonaldominant ist, konvergiert das Gesamtschrittverfahren (Jacobi) und auch das Einzelschrittverfahren (Gauss-Seidel) für Ax = b."
)
