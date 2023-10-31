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

    result = reverse_substitution(A_triangle, b)

    return A_triangle, det, result


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


Test = np.array([[1, 5, 6], [7, 9, 6], [2, 3, 4]])


b = np.array([29, 43, 20])

print(gauss_algorithm(Test, b))
