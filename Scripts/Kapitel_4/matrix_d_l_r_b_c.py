import numpy as np
import numpy.linalg as lin


def a_in_ldr_zerlegen(A):
    D = np.diag(np.diag(A))
    L = np.tril(A) - D
    R = np.triu(A) - D

    return L, D, R


def ldr_zu_b_jacobi(L, D, R):
    return -lin.inv(D).dot(L + R)


def ldr_zu_c_jacobi(D, b):
    return lin.inv(D).dot(b)


def ldr_zu_b_gauss_seidel(L, D, R):
    return -lin.inv(L + D).dot(R)


def ldr_zu_c_gauss_seidel(L, D, b):
    return lin.inv(L + D).dot(b)


########################################################################################

# Matrix definieren
A = np.array([[1, 0, 0], [2, 3, 0], [0, 1, 2]])

# Jacobi
print(f"B = \n {ldr_zu_b_jacobi(*a_in_ldr_zerlegen(A))}")
# Gauss-Seidel
print(f"B = \n {ldr_zu_b_gauss_seidel(*a_in_ldr_zerlegen(A))}")


# Vektor b definieren
# b = np.array([1, 2, 3])

# Jacobi
# print(f"C = \n {ldr_zu_c_jacobi(a_in_ldr_zerlegen(A)[1], b)}")
# Gauss-Seidel
# print(
#     f"C = \n {ldr_zu_c_gauss_seidel(a_in_ldr_zerlegen(A)[0], a_in_ldr_zerlegen(A)[1], b)}"
# )
