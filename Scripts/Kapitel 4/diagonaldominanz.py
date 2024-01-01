import numpy as np

def is_diagonally_dominant(matrix):
    rows, cols = matrix.shape
    if (check_zeilendominanz(rows) or check_spaltendominanz(cols)):
        print("Die Matrix ist diagonaldominant.")
        return True
    print("Die Matrix ist nicht diagonaldominant.")
    return False

def check_zeilendominanz(rows):
    for i in range(rows):
        diagonal = abs(matrix[i, i])
        non_diagonal_sum = np.sum(abs(matrix[i, :])) - diagonal
        if diagonal < non_diagonal_sum:
            return False
    print("Die Matrix ist zeilendominant.")
    return True
def check_spaltendominanz(cols):
    for i in range(cols):
        diagonal = abs(matrix[i, i])
        non_diagonal_sum = np.sum(abs(matrix[:, i])) - diagonal
        if diagonal < non_diagonal_sum:
            return False
    print("Die Matrix ist spaltendominant.")
    return True
        
# Variablen definieren und Funktionsaufruf
matrix = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
is_diagonally_dominant(matrix)