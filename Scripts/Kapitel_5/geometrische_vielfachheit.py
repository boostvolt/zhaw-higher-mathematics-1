import numpy as np
from numpy.linalg import matrix_rank


def geometrische_vielfachheit(A, debug=False):
    eigenvalues = np.linalg.eigvals(A)
    n = A.shape[0]
    geometric_multiplicities = {}

    # TODO: Add debug output matrix to ZSF for rank calculation

    for eigenvalue in eigenvalues:
        diff = A - eigenvalue * np.eye(n)
        rank = matrix_rank(diff)
        geometric_multiplicity = n - rank
        geometric_multiplicities[eigenvalue] = geometric_multiplicity

        if debug:
            print(f"-- Geometrische Vielfachheit zum Eigenwert λ = {eigenvalue}")
            print(
                f"A - λI_{n} = \n {np.array(A)} \n - {eigenvalue} * \n {np.array(np.eye(n))} \n = \n {np.array(diff)}"
            )
            print(f"n = {n}")
            print(f"rg(A - λI_{n}) = {rank}")
            print()

    return geometric_multiplicities


########################################################################################

# Define the matrix
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

print(f"Geometrische Vielfachheit: {geometrische_vielfachheit(A, True)}")
