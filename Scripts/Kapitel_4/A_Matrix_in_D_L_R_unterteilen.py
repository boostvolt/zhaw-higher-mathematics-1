import numpy as np


def unterteilen(A, debug=False):
    D = np.diag(np.diag(A))
    R = np.triu(A) - D
    L = np.tril(A) - D

    if debug:
        print(f"L = \n {L}")
        print(f"D = \n {D}")
        print(f"R = \n {R}")

    return L, R, D
