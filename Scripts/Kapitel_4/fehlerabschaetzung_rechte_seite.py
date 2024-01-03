import numpy as np


def absoluter_fehler(A, b, b_tilde, norm, debug=False):
    A_invertiert = np.linalg.inv(A)
    A_invertiert_norm = np.linalg.norm(A_invertiert, norm)
    b_b_tilde_norm = np.linalg.norm(b - b_tilde, norm)

    norm_symbol = norm
    if norm == np.inf:
        norm_symbol = "∞"

    if debug:
        print(f"A^-1 = \n {A_invertiert}")
        print(f"A^-1 {norm_symbol}-Norm =  {A_invertiert_norm}")
        print(f"b - b_tilde {norm_symbol}-Norm = {b_b_tilde_norm}")
        print()

    return A_invertiert_norm * b_b_tilde_norm


def relativer_fehler(A, b, b_tilde, norm, debug=False):
    A_konditionszahl = np.linalg.norm(A, norm) * np.linalg.norm(np.linalg.inv(A), norm)
    b_b_tile_norm = np.linalg.norm(b - b_tilde, norm)
    b_norm = np.linalg.norm(b, norm)
    result = A_konditionszahl * (b_b_tile_norm / b_norm)

    norm_symbol = norm
    if norm == np.inf:
        norm_symbol = "∞"

    if debug:
        print(f"cond(A) = {A_konditionszahl}")
        print(f"b - b_tilde {norm_symbol}-Norm = {b_b_tile_norm}")
        print(f"b {norm_symbol}-Norm = {b_norm}")
        print()

    return result


########################################################################################

# Matrix A definieren
A = np.array([[2, 4], [4, 8.1]])

# Vektor b definieren
b = np.array([1, 1.5])

# Vektor b_tilde definieren
b_tilde = np.array([1.1, 1.6])

# Norm definieren (1, 2, np.inf)
norm = np.inf

print(f"Absoluter Fehler: {absoluter_fehler(A, b, b_tilde, norm, True)}")
print(f"Relativer Fehler: {absoluter_fehler(A, b, b_tilde, norm, True)}")
