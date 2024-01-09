import numpy as np


def matrix_konditionszahl(matrix, norm, debug=False):
    matrix_invertiert = np.linalg.inv(matrix)
    matrix_norm = np.linalg.norm(matrix, norm)
    matrix_invertiert_norm = np.linalg.norm(matrix_invertiert, norm)
    matrix_cond = np.dot(matrix_norm, matrix_invertiert_norm)

    if debug:
        norm_symbol = norm
        if norm == np.inf:
            norm_symbol = "∞"

        print("")
        print("Konditionszahl-Matrix")
        print(f"A {norm_symbol}-Norm = {matrix_norm}")
        print(f"A^-1 = \n{matrix_invertiert}")
        print(f"A^-1 {norm_symbol}-Norm =  {matrix_invertiert_norm}")
        print(f"cond(A){norm_symbol} = ||A||{norm_symbol} = ||A||{norm_symbol} * ||A^-1||{norm_symbol} = ")
        print(f"{matrix_norm} * {matrix_invertiert_norm} = {matrix_cond}")
        print(f"cond(A){norm_symbol} = {matrix_cond}")
        print()

    return matrix_cond


########################################################################################

# Matrix definieren
# matrix = np.array([[2, 4], [4, 8.1]])
# matrix = np.array([[1, 0, 2], [0, 1, 0], [10**(-4), 0, 10**(-4)]])

# Norm definieren (1, 2, np.inf)
norm = np.inf

# print(f"Konditionszahl: {matrix_konditionszahl(matrix, norm, debug=True)}")
