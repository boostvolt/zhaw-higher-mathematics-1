import numpy as np


def gaussian_algorithm(matrix, result_vector):
    # Convert inputs to float for precision
    matrix = matrix.astype(np.float64)
    result_vector = result_vector.astype(np.float64)

    n = len(matrix)
    matrix_top_triangle = np.copy(matrix)
    det_a = 1

    for column in range(n):
        # Find the row with the lowest index which is not zero in the current column
        non_zero_rows = np.nonzero(matrix_top_triangle[column:, column])[0]
        if non_zero_rows.size == 0:
            raise ValueError("Error: A column is all zero")
        first_non_zero_row = column + non_zero_rows[0]

        # If the first non-zero row is not the current row, swap them
        if column != first_non_zero_row:
            matrix_top_triangle[[column, first_non_zero_row]] = matrix_top_triangle[
                [first_non_zero_row, column]
            ]
            det_a *= -1

        # Make all rows below this one 0 in the current column
        for row in range(column + 1, n):
            factor = (
                matrix_top_triangle[row, column] / matrix_top_triangle[column, column]
            )
            matrix_top_triangle[row, column:] -= (
                factor * matrix_top_triangle[column, column:]
            )
            result_vector[row] -= factor * result_vector[column]

    # Calculate the determinant
    det_matrix = det_a * np.prod(np.diag(matrix_top_triangle))

    # Check if the determinant is zero
    if det_matrix == 0:
        raise ValueError("Error: det is zero")

    # Perform back substitution to solve for x
    x = reverse_substitution(matrix_top_triangle, result_vector)

    return matrix_top_triangle, det_matrix, x


def reverse_substitution(matrix, result_vector):
    n = len(matrix)
    x = np.zeros(n)

    for diagonal in range(n - 1, -1, -1):
        x[diagonal] = (
            result_vector[diagonal]
            - np.dot(matrix[diagonal, diagonal + 1 :], x[diagonal + 1 :])
        ) / matrix[diagonal, diagonal]

    return x


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


def calc_det(matrix):
    result = 1
    for diagonal in range(len(matrix) - 1, -1, -1):
        result *= matrix[diagonal, diagonal]

    return result


print("A1", gaussian_algorithm(A1, b1))
print("A2", gaussian_algorithm(A2, b2))
print("A3", gaussian_algorithm(A3, b3))
print("A4", gaussian_algorithm(A4, b4))

print("numpy A1", np.linalg.solve(A1, b1))
print("numpy A2", np.linalg.solve(A2, b2))
print("numpy A3", np.linalg.solve(A3, b3))
print("numpy A4", np.linalg.solve(A4, b4))
