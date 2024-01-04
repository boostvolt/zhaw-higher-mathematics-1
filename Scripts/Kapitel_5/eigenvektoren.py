import numpy as np
import sympy as sp


def eigenvektoren(A):
    A = sp.Matrix(A)

    # TODO: Add debug output for eigenvektoren calculation

    data = A.eigenvects()
    for _, values in enumerate(data):
        for vec in values[2]:
            print(f"\nEigenvektor(en) zu Eigenwert λ = {values[0]}: \n {np.array(vec)}")


########################################################################################

# Matrix A definieren
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

eigenvektoren(A)
