import numpy as np
from IT22ta_WIN10_S6_Aufg2 import gaussian_algorithm

A1 = np.array([[4, -1, -5], [-12, 4, 17], [32, -10, -41]])
b1 = np.array([6, -12, 48])

A2 = np.array([[2, 7, 3], [-4, -10, 0], [12, 34, 9]])
b2 = np.array([5, -22, 42])

A3 = np.array([[-2, 5, 4], [-14, 38, 22], [6, -9, -27]])
b3 = np.array([16, 82, -120])

A4 = np.array(
    [
        [-1, 2, 3, 2, 5, 4, 3, -1],
        [3, 4, 2, 1, 0, 2, 3, 8],
        [2, 7, 5, -1, 2, 1, 3, 5],
        [3, 1, 2, 6, -3, 7, 2, -2],
        [5, 2, 0, 8, 7, 6, 1, 3],
        [-1, 3, 2, 3, 5, 3, 1, 4],
        [8, 7, 3, 6, 4, 9, 7, 9],
        [-3, 14, -2, 1, 0, -2, 10, 5],
    ]
)
b4 = np.array([-11, 103, 53, -20, 95, 78, 131, -26])

print("A1", gaussian_algorithm(A1, b1))
print("A2", gaussian_algorithm(A2, b2))
print("A3", gaussian_algorithm(A3, b3))
print("A4", gaussian_algorithm(A4, b4))

print("numpy A1", np.linalg.solve(A1, b1), np.linalg.det(A1))
print("numpy A2", np.linalg.solve(A2, b2), np.linalg.det(A2))
print("numpy A3", np.linalg.solve(A3, b3), np.linalg.det(A3))
print("numpy A4", np.linalg.solve(A4, b4), np.linalg.det(A4))

# Numpy's linalg.solve uses partial pivoting, which can help maintain numerical stability. Our Gaussian elimination algorithm does not use pivoting, this can lead to large numerical errors.
