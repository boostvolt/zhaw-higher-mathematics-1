import numpy as np


def eigenwerte(A):
    return np.linalg.eigvals(A)


########################################################################################

# Matrix A definieren
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

print(f"Eigenwerte: {eigenwerte(A)}")
