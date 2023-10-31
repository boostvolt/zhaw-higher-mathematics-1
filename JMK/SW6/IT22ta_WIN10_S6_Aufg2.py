import numpy as np


def gaussian_elimination_algorithm(matrix, result_vector):
    matrix = matrix.astype(np.float64)
    result_vector = result_vector.astype(np.float64)

    n = len(matrix)
    matrix_top_triangle = np.copy(matrix).astype(np.float64)
    det_a = 1

    for column in range(n):
        if matrix_top_triangle[column, column] == 0:
            zero_columns = 0
            for row in range(column + 1, n):
                if matrix_top_triangle[row, column] == 0:
                    zero_columns += 1
                else:
                    current_row = np.copy(matrix_top_triangle[column, :])
                    for row_next_value in range(column + 1, n):
                        if (
                            row_next_value >= column + 1
                            and matrix_top_triangle[row_next_value, column] != 0
                        ):
                            matrix_top_triangle[column, :] = matrix_top_triangle[
                                row_next_value, :
                            ]
                            matrix_top_triangle[row_next_value, :] = current_row
                            det_a *= -1

            if zero_columns == n - column - 1:
                raise ValueError("Error: A column is all zero")

        for row in range(column + 1, n):
            factor = (
                matrix_top_triangle[row, column] / matrix_top_triangle[column, column]
            )
            matrix_top_triangle[row, column:] -= (
                factor * matrix_top_triangle[column, column:]
            )
            result_vector[row] -= factor * result_vector[column]

    det_matrix = calc_det(matrix_top_triangle, det_a)

    if det_matrix == 0:
        raise ValueError("Error: det is zero")

    return (
        matrix_top_triangle,
        det_matrix,
        reverse_substitution(matrix_top_triangle, result_vector),
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


