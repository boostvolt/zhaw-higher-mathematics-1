import numpy as np


def matrix_norm(matrix, norm):
    norm_symbol = norm
    if norm == np.inf:
        norm_symbol = "∞"

    # TODO: Add debug output

    return norm_symbol, np.linalg.norm(matrix, norm)


########################################################################################

# Matrix definieren
matrix = np.array([[5, -2], [0, -6]])

# Norm definieren (1, 2, np.inf)
norm = np.inf

[norm_symbol, norm] = matrix_norm(matrix, norm)
print(f"Matrix {norm_symbol}-Norm: {norm}")
