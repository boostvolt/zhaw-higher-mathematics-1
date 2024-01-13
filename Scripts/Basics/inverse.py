import numpy as np


def inverse(A):
    return np.linalg.inv(A)


########################################################################################

# Matrix definieren
A = np.array([[4, 1, 0], [3, 2, 1], [5, 2, -1]])

print(f"Inverse: \n {inverse(A)}")
