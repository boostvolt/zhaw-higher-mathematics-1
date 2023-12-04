import numpy as np


def gaussian_algorithm(matrix, result_vector):
    matrix = np.copy(matrix).astype(np.float64)
    result_vector = np.copy(result_vector).astype(np.float64)

    if len(matrix) != len(matrix[0]):
        raise ValueError("Error: The matrix is not square")

    if len(matrix) != len(result_vector):
        raise ValueError("Error: The matrix and result vector have different sizes")

    n = len(matrix)
    det_a = 1

    for column in range(n):
        if matrix[column, column] == 0:
            zero_columns = 0
            for row in range(column + 1, n):
                if matrix[row, column] == 0:
                    zero_columns += 1
                else:
                    for row_next_value in range(column + 1, n):
                        current_row_matrix = np.copy(matrix[column, :])
                        current_row_result = np.copy(result_vector[column])

                        if (
                            row_next_value >= column + 1
                            and matrix[row_next_value, column] != 0
                        ):
                            matrix[column, :] = matrix[row_next_value, :]
                            matrix[row_next_value, :] = current_row_matrix
                            result_vector[column] = result_vector[row_next_value]
                            result_vector[row_next_value] = current_row_result

                            det_a *= -1

            if zero_columns == n - column - 1:
                raise ValueError("Error: A column is all zero")

        for row in range(column + 1, n):
            factor = matrix[row, column] / matrix[column, column]
            matrix[row, column:] -= factor * matrix[column, column:]
            result_vector[row] -= factor * result_vector[column]

    det_a = calc_det(matrix, det_a)

    if det_a == 0:
        raise ValueError("Error: det is zero")

    return (
        matrix,
        det_a,
        reverse_substitution(matrix, result_vector),
    )


def reverse_substitution(matrix, result_vector):
    n = len(matrix)
    x = np.zeros(n)
    for diagonal in range(n - 1, -1, -1):
        for column in range(diagonal + 1, n):
            result_vector[diagonal] -= matrix[diagonal, column] * x[column]

        x[diagonal] = result_vector[diagonal] / matrix[diagonal, diagonal]

    return x


def calc_det(matrix, det_a):
    for diagonal in range(len(matrix) - 1, -1, -1):
        det_a *= matrix[diagonal, diagonal]

    return det_a
