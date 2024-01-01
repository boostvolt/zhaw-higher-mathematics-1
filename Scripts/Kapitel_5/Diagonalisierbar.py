import numpy as np


def is_diagonal(matrix):
    # Extract the diagonal elements of the matrix
    diagonal_elements = np.diag(matrix)

    # Create a new diagonal matrix with the diagonal elements
    diagonal_matrix = np.diagflat(diagonal_elements)

    # Check if the new matrix is equal to the original matrix
    return np.array_equal(matrix, diagonal_matrix)


def ist_diagonalisierbar(A, T, debug: False):
    D = np.linalg.inv(T) @ A @ T
    if is_diagonal(D):
        eigenwerte = np.diag(D)
        eigenvektoren = []
        for i in range(T.shape[1]):
            eigenvektoren.append(T[:, i])
        if debug:
            print("D = T^-1 * A * T")
            print(f"{np.linalg.inv(T)} \n*\n {A} \n*\n {T} \n=\n {D}")
            print("Eigenwerte: ", eigenwerte)
            print("Eigenvektoren: ", eigenvektoren)

        print("Die Matrix ist diagonalisierbar")
    else:
        print("Die Matrix ist nicht diagonalisierbar")

    return eigenwerte, eigenvektoren


# A = np.array([[3, 1, -1], [2, 4, -2], [1, 1, 1]])
# T = np.array([[1, 1, 1], [0, 2, 1], [1, 1, 2]])

A = np.array([[2, 0, 1], [7, -5, 9], [6, -6, 9]])
T = np.array([[3, 1, 1], [-1, 1, 2], [-3, 0, 1]])

ist_diagonalisierbar(A, T, True)
