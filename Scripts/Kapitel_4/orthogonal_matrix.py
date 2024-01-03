import numpy as np


def is_orthogonal(A):
    A = np.array(A)

    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(
            "A muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )

    return np.allclose(np.dot(A, A.T), np.eye(A.shape[0]))


########################################################################################

# Matrix A definieren
A = np.array([[2 / 3, -2 / 3, -1 / 3], [1 / 3, 2 / 3, -2 / 3], [2 / 3, 1 / 3, 2 / 3]])

print(f"Orthogonal: {is_orthogonal(A)}")
