import numpy as np


def insert_backwards(A, b):
    x = np.zeros((len(A), 1))
    for i in range(len(A) - 1, -1, -1):  # start at the end and go backwards
        x[i] = (b[i] - np.dot(A[i, i + 1 :], x[i + 1 :])) / A[i, i]
    return x


def solve_linalg_sys(A, b):
    if A.shape[0] != A.shape[1] or A.shape[0] != b.shape[0]:
        raise Exception(
            "Matrix must be a square matrix and dim of rows must match between A and b."
        )

    for i in range(0, len(A)):
        if np.count_nonzero(A[:, i]) == 0:
            raise Exception("Matrix is not regular due to all zero row.")

    count_of_row_switches = 0
    for i in range(0, len(A)):
        count_of_row_switches += sort_column(A, b, i)
        elimination_step(A, b, i)

    det = 1
    for i in range(0, len(A)):
        det *= A[i, i]
    det = ((-1) ** count_of_row_switches) * det

    x = insert_backwards(A, b)

    return [A, det, x]


def sort_column(A, b, i):
    if A[i, i] == 0:
        for j in range(0, len(A)):
            if A[j, i] != 0:
                break
        A[[i, j]] = A[[j, i]]
        b[[i, j]] = b[[j, i]]
        return 1
    return 0


def elimination_step(A, b, diag_idx):
    curr_diagonal_number = A[diag_idx, diag_idx]
    for row_idx in range(diag_idx + 1, len(A)):
        curr_lambda = A[row_idx, diag_idx] / curr_diagonal_number
        A[row_idx, :] = calc_new_row(curr_lambda, A[row_idx, :], A[diag_idx, :])
        b[row_idx] = calc_new_row(curr_lambda, b[row_idx], b[diag_idx])


def calc_new_row(curr_lambda, curr_row, comp_row):
    for i in range(0, len(curr_row)):
        curr_row[i] = curr_row[i] - curr_lambda * comp_row[i]
    return curr_row
