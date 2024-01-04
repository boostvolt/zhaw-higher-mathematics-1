import numpy as np
import sympy as sp


def charakteristisches_polynom(A, debug=False):
    A = sp.matrices.Matrix(A)
    lambda_symbol = sp.symbols("λ")
    I = sp.matrices.eye(A.shape[0])
    polynom = A.charpoly(lambda_symbol).as_expr()
    factorized_polynom = sp.factor(polynom)

    if debug:
        print("-- Charakteristisches Polynom")
        print(
            f"A - λI_{A.shape[0]} = \n {np.array(A)} \n - λ * \n {np.array(I)} \n = \n {np.array(A - lambda_symbol * I)}"
        )
        print(f"det(A - λI_{A.shape[0]}) = p(λ) = {polynom} = {factorized_polynom}")

    return polynom, factorized_polynom


########################################################################################

# Matrix A definieren
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

charakteristisches_polynom(A, True)
