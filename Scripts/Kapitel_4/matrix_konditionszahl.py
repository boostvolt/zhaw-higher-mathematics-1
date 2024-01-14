import numpy as np


def matrix_konditionszahl(matrix, norm, debug=False):
    print(f"************{matrix}")
    matrix_invertiert = np.linalg.inv(matrix)
    matrix_norm = np.linalg.norm(matrix, norm)
    matrix_invertiert_norm = np.linalg.norm(matrix_invertiert, norm)
    matrix_cond = np.dot(matrix_norm, matrix_invertiert_norm)

    if debug:
        norm_symbol = norm
        if norm == np.inf:
            norm_symbol = "∞"
        print(f"||A||_{norm_symbol} = {matrix_norm}")
        print()

        print(f"A^-1 = \n {matrix_invertiert}")
        print(f"||A^-1||_{norm_symbol} = {matrix_invertiert_norm}")
        print()

        print(
            f"cond_{norm_symbol}(A) = ||A||_{norm_symbol} * ||A^-1||_{norm_symbol}: \n {matrix_norm} * {matrix_invertiert_norm} \n = {matrix_cond}"
        )
        print()

    return matrix_cond


########################################################################################
if __name__ == "__main__":
    # Matrix definieren
    matrix = np.array([[2, 4], [4, 8.1]])

    # Norm definieren (1, 2, np.inf)
    norm = np.inf

    print(f"Konditionszahl: {matrix_konditionszahl(matrix, norm, debug=True)}")
