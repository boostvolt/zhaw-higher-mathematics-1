import numpy as np
import sympy as sp
from geometrische_vielfachheit import geometrische_vielfachheit


def eigenvektoren(A, debug=False):
    data = sp.Matrix(A).eigenvects()

    for _, values in enumerate(data):
        geometrische_vielfachheit(A, True, [float(values[0])])

        if debug:
            print("-- Eigenvektor(en)")
        for vec in values[2]:
            if debug:
                print(f"{np.array(vec)}")
                print()

    return data


########################################################################################

# Matrix A definieren
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

eigenvektoren(A, True)
