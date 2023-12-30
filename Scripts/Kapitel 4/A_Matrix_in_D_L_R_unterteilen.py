import numpy as np

def unterteilen(A):
    D = np.diag(np.diag(A))
    R = np.triu(A) - D
    L = np.tril(A) - D
    return L, R, D