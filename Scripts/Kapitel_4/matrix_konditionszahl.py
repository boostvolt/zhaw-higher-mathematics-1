import numpy as np


def matrix_konditionszahl(matrix, norm, debug=False):
    matrix_norm = np.linalg.norm(matrix, norm)
    matrix_invertiert_norm = np.linalg.norm(np.linalg.inv(matrix), norm)

    if debug:
        norm_symbol = norm
        if norm == np.inf:
            norm_symbol = "∞"

        print(f"Matrix {norm_symbol}-Norm: {matrix_norm}")
        print(f"Invertierte Matrix {norm_symbol}-Norm: {matrix_invertiert_norm}")
        print()

    return np.dot(matrix_norm, matrix_invertiert_norm)


########################################################################################

# Matrix definieren
matrix = np.array([[2, 4], [4, 8.1]])

# Norm definieren (1, 2, np.inf)
norm = np.inf

print(f"Konditionszahl: {matrix_konditionszahl(matrix, norm, debug=True)}")
