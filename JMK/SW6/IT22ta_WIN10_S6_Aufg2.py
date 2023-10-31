import numpy as np


def gauss_algorithm(A, b):
    A = A.astype(np.float64)
    b = b.astype(np.float64)

    n = len(A)
    A_triangle = np.copy(A).astype(np.float64)

    for column in range(n):
        if A_triangle[column, column] == 0:
            zero_columns = 0
            for row in range(column + 1, n):
                if A_triangle[row, column] == 0:
                    zero_columns += 1
                else:
                    current_row = np.copy(A_triangle[column, :])
                    for row_next_value in range(column + 1, n):
                        if (
                            row_next_value >= column + 1
                            and A_triangle[row_next_value, column] != 0
                        ):
                            A_triangle[column, :] = A_triangle[row_next_value, :]
                            A_triangle[row_next_value, :] = current_row

            if zero_columns == n - column - 1:
                raise ValueError("Error: A column is all zero")

        for row in range(column + 1, n):
            factor = A_triangle[row, column] / A_triangle[column, column]
            A_triangle[row, column:] -= factor * A_triangle[column, column:]
            b[row] -= factor * b[column]

    det = calc_det(A_triangle)

    if det == 0:
        raise ValueError("Error: det is zero")

    return A_triangle, det, reverse_substitution(A_triangle, b)


def reverse_substitution(A, b):
    n = len(A)
    x = np.zeros(n)
    for diagonal in range(n - 1, -1, -1):
        for column in range(diagonal + 1, n):
            b[diagonal] -= A[diagonal, column] * x[column]

        x[diagonal] = b[diagonal] / A[diagonal, diagonal]

    return x


def calc_det(A):
    result = 1
    for diagonal in range(len(A) - 1, -1, -1):
        result *= A[diagonal, diagonal]
    return result


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


simon_matrix = np.array([[0, -1, -5], [-12, 4, 17], [32, -10, -41]], dtype=float)

print(calc_det(simon_matrix))

print("A1", gauss_algorithm(A1, b1))
print("A2", gauss_algorithm(A2, b2))
print("A3", gauss_algorithm(A3, b3))
print("A4", gauss_algorithm(A4, b4))

print("numpy A1", np.linalg.solve(A1, b1))
print("numpy A2", np.linalg.solve(A2, b2))
print("numpy A3", np.linalg.solve(A3, b3))
print("numpy A4", np.linalg.solve(A4, b4))

#
