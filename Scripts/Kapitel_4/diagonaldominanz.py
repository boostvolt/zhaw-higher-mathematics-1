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
        if diagonal < non_diagonal_sum:
            return False

    if debug:
        print("Zeilendominant")
        print()

    return True


def check_spaltendominanz(cols, debug=False):
    for i in range(cols):
        diagonal = abs(matrix[i, i])
        non_diagonal_sum = np.sum(abs(matrix[:, i])) - diagonal
        if diagonal < non_diagonal_sum:
            return False

    if debug:
        print("Spaltendominant")
        print()

    return True


########################################################################################

# Matrix definieren
matrix = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])

print(f"Diagonaldominanz: {is_diagonaldominant(matrix, True)}")
