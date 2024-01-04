import numpy as np
from geometrische_vielfachheit import geometrische_vielfachheit


def eigenvektoren(A, debug=False):
    eigenvalues, eigenvectors = np.linalg.eig(A)

    for i in range(len(eigenvalues)):
        eigenvalue = eigenvalues[i]
        eigenvector = eigenvectors[:, i]

        geometrische_vielfachheit(A, True, [eigenvalue])

        if debug:
            print("-- Eigenvektor(en)")
            print(f"{eigenvector.reshape(-1, 1)}")
            print()

    return eigenvectors


########################################################################################

# Matrix A definieren
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

eigenvektoren(A, True)
