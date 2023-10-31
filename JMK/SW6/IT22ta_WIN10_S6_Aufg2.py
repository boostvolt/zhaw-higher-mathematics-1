import numpy as np

# i = row zeile
# j = column spalte


def gauss_algorithm(A, b):
    n = len(A)
    A_triangle = np.copy(A)
    detA = 1

    for column in range(n):
        if A_triangle[column, column] == 0:
            zero_columns = 0
            for row in range(column + 1, n):
                if A_triangle[row, column] == 0:
                    zero_columns += 1
                else:
                    current_row = A_triangle[row, column]
                    for row_next_value in range(column + 1, n):
                        if (
                            row_next_value >= column + 1
                            and A_triangle[row_next_value, column] != 0
                        ):
                            A_triangle[row, column] = A_triangle[row_next_value, column]
                            A_triangle[row_next_value, column] = current_row

                # if A_triangle[row, column + 1] != 0:
                #     initial_row = row
                #     row = column + 1
                #     while A_triangle[row, column] == 0:
                #         row += 1

                # A_triangle[initial_row:column]

            if zero_columns == n - column - 1:
                raise ValueError("Error: A column is all zero")


Test = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])


b = np.array([150, 470, 2150])

print(gauss_algorithm(Test, b))
