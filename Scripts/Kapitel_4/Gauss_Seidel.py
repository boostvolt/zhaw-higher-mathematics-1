import numpy as np
import numpy.linalg as lin


def a_in_ldr_lerlegen(A, debug=False):
    D = np.diag(np.diag(A))
    L = np.tril(A) - D
    R = np.triu(A) - D

    if debug:
        print("-- A in (L + D)^-1, R zerlegen")
        print(f"(L + D)^-1 = \n {lin.inv(L + D)}")
        print(f"R = \n {R}")
        print()

    return D, L, R


def ldr_zu_bc(D, L, R, b, debug=False):
    B = -lin.inv(L + D).dot(R)
    C = lin.inv(L + D).dot(b.reshape(-1, 1))

    if debug:
        print("-- Von (L + D)^-1, R zu B, C")
        print(f"B = -(L + D)^-1 * R = \n {B}")
        print(f"C = (L + D)^-1 * b = \n {C}")
        print()

    return B, C


def gauss_seidel_iteration(B, C, prev_x, debug=False):
    if debug:
        print(f" {B} \n * \n {prev_x.reshape(-1, 1)} \n + \n {C}")

    return B.dot(prev_x.reshape(-1, 1)) + C


def vergleiche_toleranz(prev_value, next_value, toleranz):
    for i in range(len(prev_value)):
        if np.abs(prev_value[i] - next_value[i]) > toleranz:
            return False

    return True


def gauss_seidel_mit_toleranz(A, b, x_0, toleranz, debug=False):
    previous_value = x_0
    next_x_value = np.full(len(previous_value), -100)
    iteration_count = 0

    [D, L, R] = a_in_ldr_lerlegen(A, debug)
    [B, C] = ldr_zu_bc(D, L, R, b, debug)

    while not vergleiche_toleranz(previous_value, next_x_value, toleranz):
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            previous_value = next_x_value

        if debug:
            print(f"--------------------- Iteration: {iteration_count + 1}")
            print(f"x^{iteration_count + 1} = B * x^{iteration_count} + C =")

        next_x_value = gauss_seidel_iteration(B, C, previous_value, debug)
        print(f" = \n {next_x_value}")
        print()

        iteration_count = iteration_count + 1

    return next_x_value


def gauss_seidel_mit_anzahl_iterationen(A, b, x_0, iterationen, debug=False):
    previous_value = x_0
    next_x_value = -100
    x_values = [previous_value]

    [D, L, R] = a_in_ldr_lerlegen(A, debug)
    [B, C] = ldr_zu_bc(D, L, R, b, debug)

    for i in range(iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value

        next_x_value = gauss_seidel_iteration(B, C, previous_value, debug)
        x_values.append(next_x_value)
        print(f" = \n {next_x_value}")
        print()

    return x_values


########################################################################################

# Matrix A definieren
A = np.array([[4, -1, 1], [-2, 5, 1], [1, -2, 5]])

# Vektor b definieren
b = np.array([5, 11, 12])

# Startvektor x_0 definieren
x_0 = np.array([0, 0, 0])

# Fixpunkt mit Toleranz berechnen
# Toleranz definieren
toleranz = 10**-4

gauss_seidel_mit_toleranz(A, b, x_0, toleranz, True)

# Fixpunkt mit angegebener Anzahl Iterationen berechnen
# Anzahl der Iterationen
# iterationen = 2

# gauss_seidel_mit_anzahl_iterationen(A, b, x_0, iterationen, True)
