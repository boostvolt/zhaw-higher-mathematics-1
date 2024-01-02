import numpy as np

def matrix_absoluter_fehler(A, debug=False):
    A_invertiert = np.linalg.inv(A)
    result = np.linalg.norm(A_invertiert, np.inf) * np.linalg.norm(b - b_tilde, np.inf)
    if debug:
        print(f"A^-1: {A_invertiert}")
        print(f"b: {b}")
        print(f"b_tilde: {b_tilde}")
        print(f"Der absolute Fehler beträgt: {result}")
    return result

def matrix_relativer_fehler(A, debug=False):
    A_invertiert = np.linalg.inv(A)
    A_konditionszahl = np.linalg.norm(A, np.inf) * np.linalg.norm(np.linalg.inv(A), np.inf)
    b_b_tile_norm = np.linalg.norm(b - b_tilde, np.inf)
    b_norm = np.linalg.norm(b, np.inf)
    result = A_konditionszahl * (b_b_tile_norm / b_norm)
    if debug:
        print(f"A^-1: {A_invertiert}")
        print(f"b: {b}")
        print(f"b_norm: {b_norm}")
        print(f"Norm von b - b_tilde: {b_b_tile_norm}")
        print(f"b_tilde: {b_tilde}")
        print(f"Der relative Fehler beträgt: {result}")
    return result

A = np.array([[2, 4], [4, 8.1]])
b = np.array([1, 1.5])
b_tilde = np.array([1.1, 1.6])

# Funktionsaufruf mit Debug-Mode
matrix_absoluter_fehler(A, True)
matrix_relativer_fehler(A, True)
