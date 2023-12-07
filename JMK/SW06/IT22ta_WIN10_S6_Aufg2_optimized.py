import numpy as np


def gaussian_algorithm(matrix, result_vector):
    matrix = np.copy(matrix.astype(np.float64))
    result_vector = np.copy(result_vector.astype(np.float64))

    if len(matrix) != len(matrix[0]):
        raise ValueError("Error: The matrix is not square")

    if len(matrix) != len(result_vector):
        raise ValueError("Error: The matrix and result vector have different sizes")

    n = len(matrix)
    det = 1

    for column in range(n):
        # Find the row with the lowest index which is not zero in the current column
        non_zero_rows = np.nonzero(matrix[column:, column])[0]
        if non_zero_rows.size == 0:
            raise ValueError("Error: A column is all zero")
        first_non_zero_row = column + non_zero_rows[0]

        # If the first non-zero row is not the current row, swap them
        if column != first_non_zero_row:
            matrix[[column, first_non_zero_row]] = matrix[[first_non_zero_row, column]]
            result_vector[[column, first_non_zero_row]] = result_vector[
                [first_non_zero_row, column]
            ]

            det *= -1

        # Make all rows below this one 0 in the current column
        for row in range(column + 1, n):
            factor = matrix[row, column] / matrix[column, column]
            matrix[row, column:] -= factor * matrix[column, column:]
            result_vector[row] -= factor * result_vector[column]

    # Calculate the determinant
    det_matrix = det * np.prod(np.diag(matrix))

    # Check if the determinant is zero
    if det_matrix == 0:
        raise ValueError("Error: det is zero")

    # Perform back substitution to solve for x
    x = reverse_substitution(matrix, result_vector)

    return matrix, det_matrix, x


def reverse_substitution(matrix, result_vector):
    n = len(matrix)
    x = np.zeros(n)

    for diagonal in range(n - 1, -1, -1):
        x[diagonal] = (
            result_vector[diagonal]
            - np.dot(matrix[diagonal, diagonal + 1 :], x[diagonal + 1 :])
        ) / matrix[diagonal, diagonal]

    return x
