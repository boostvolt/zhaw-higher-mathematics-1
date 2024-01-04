import numpy as np
from numpy.linalg import matrix_rank


def matrix_in_zsf(matrix, debug=False):
    matrix = np.array(matrix)
    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError(
            "Muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )

    n = len(matrix)

    print(f"---- A - λI_{matrix.shape[0]} auf ZSF bringen")

    for i in range(n):
        if matrix[i][i] == 0:
            continue

        for j in range(i + 1, n):
            if matrix[j][i] != 0:
                factor = matrix[j][i] / matrix[i][i]

                if debug:
                    print("---- Nächster Schritt")
                    print(matrix)

                matrix[j] = matrix[j] - factor * matrix[i]

                if debug:
                    print(f"Zeile {j + 1} - ({factor}) · Zeile {i + 1}")
                    print(matrix)
                    print()

    if debug:
        print("---- Abgeschlossene Zerlegung")
        print(f"A - λI_{matrix.shape[0]} = \n {matrix}")
        print()

    return matrix


def geometrische_vielfachheit(A, debug=False, eigenvalues=None):
    n = A.shape[0]
    geometric_multiplicities = {}

    if eigenvalues is None:
        eigenvalues = list(np.linalg.eigvals(A))

    for eigenvalue in eigenvalues:
        if not any(isinstance(eigenvalue, complex) for eigenvalue in eigenvalues):
            eigenvalue = round(eigenvalue, 10)

        diff = A - eigenvalue * np.eye(n)
        rank = matrix_rank(diff)
        geometric_multiplicity = n - rank
        geometric_multiplicities[eigenvalue] = geometric_multiplicity

        if debug:
            print(f"-- Geometrische Vielfachheit zum Eigenwert λ = {eigenvalue}")
            print(
                f"A - λI_{n} = \n {np.array(A)} \n - {eigenvalue} * \n {np.array(np.eye(n))} \n = \n {np.array(diff)}"
            )
            print()
            matrix_in_zsf(diff, debug)
            print(f"n - rg(A - λI_{n}) = {n} - {rank} = {n - rank} Eigenvektor(en)")
            print()

    return geometric_multiplicities


########################################################################################
if __name__ == "__main__":
    # Matrix A definieren
    A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

    print(f"Geometrische Vielfachheit: {geometrische_vielfachheit(A, True)}")
