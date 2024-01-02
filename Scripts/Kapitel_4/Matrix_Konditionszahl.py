import numpy as np

def matrix_konditionszahl(matrix, norm, debug=False):
    if (norm == np.inf):
        norm_sign = "∞"
    else: 
        norm_sign = norm

    matrix_norm = np.linalg.norm(matrix, norm)
    print(f"Norm der Matrix: {matrix_norm}")
    matrix_invertiert = np.linalg.inv(matrix)
    matrix_invertiert_norm = np.linalg.norm(matrix_invertiert, norm)
    print(f"Norm der invertierten Matrix: {matrix_invertiert_norm}")
    konditionszahl = np.dot(matrix_norm, matrix_invertiert_norm)
    print(f"Konditionszahl der Matrix {matrix} beträgt: {konditionszahl}")
    if debug:
        print(f"\nEinzelne Schritte: \n\n----------\ncond{norm_sign}(A) \n= ||A||{norm_sign}||A^-1||{norm_sign} \n= ||{matrix}||{norm_sign}||{matrix_invertiert}||{norm_sign} \n= {matrix_norm} * {matrix_invertiert_norm}\n={konditionszahl}\n----------")
    return konditionszahl

# Matrix definieren
A = np.array([[4, 0], [0, 4]])
# Norm definieren
# Unendlichkeitsnorm
norm = np.inf
# 2. Norm
# norm = 2

matrix_konditionszahl(A, norm, debug=True)