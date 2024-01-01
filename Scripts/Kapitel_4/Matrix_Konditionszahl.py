import numpy as np

def matrix_konditionszahl(matrix):
    matrix_norm = np.linalg.norm(matrix, np.inf)
    print(f"Norm der Matrix: {matrix_norm}")
    matrix_invertiert_norm = np.linalg.norm(np.linalg.inv(matrix), np.inf)
    print(f"Norm der invertierten Matrix: {matrix_invertiert_norm}")
    konditionszahl = np.dot(matrix_norm, matrix_invertiert_norm)
    print(f"Konditionszahl der Matrix {matrix} beträgt: {konditionszahl}")
    return konditionszahl

A = np.array([[2, 4], [4, 8.1]])
matrix_konditionszahl(A)