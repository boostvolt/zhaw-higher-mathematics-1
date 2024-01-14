import matrix_konditionszahl as kondition
import numpy as np
import sympy as sp


def convert_norm(norm):
    if norm == np.inf:
        return "∞"
    else:
        return norm


def berechne_x(A, b, debug=False):
    if debug:
        print(f"A \n=\n{A}")
        print(f"b\n=\n{b}")
        print()
    return np.linalg.solve(A, b)


def berechne_x_tilde(A, b_tilde, debug=False):
    if debug:
        print(f"A \n=\n{A}")
        print(f"b_tilde \n=\n{b_tilde}")
        print()
    return np.linalg.solve(A, b_tilde)


def tatsächlicher_absoluter_fehler(A, b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    x = berechne_x(A, b, True)
    x_tilde = berechne_x_tilde(A, b_tilde, True)
    x_minus_x_tilde = x - x_tilde
    absoluter_fehler = np.linalg.norm(x_minus_x_tilde, norm)

    if debug:
        print("---------- Tatsächlicher absoluter Fehler ----------")
        print(f"x = {x}")
        print(f"x̄ = {x_tilde}")
        print(f"||x̄ - x||{norm_symbol} \n=\n{x_minus_x_tilde}")
        print(
            f"Tatsächlicher absoluter Fehler bezüglich der {norm_symbol}-Norm: {absoluter_fehler}"
        )
        print()

    return absoluter_fehler


def tatsächlicher_relativer_fehler(A, b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    x = berechne_x(A, b)
    x_tilde = berechne_x_tilde(A, b_tilde)
    x_minus_x_tilde = x - x_tilde
    x_minus_x_tilde_norm = np.linalg.norm(x_minus_x_tilde, norm)
    x_norm = np.linalg.norm(x, norm)
    relativer_fehler = x_minus_x_tilde_norm / x_norm

    if debug:
        print("---------- Tatsächlicher relativer Fehler ----------")
        print(f"x = {x}")
        print(f"x̄ = {x_tilde}")
        print(f"||x̄ - x||{norm_symbol} \n=\n{x_minus_x_tilde}")
        print(f"||x||{norm_symbol} = {x_norm}")
        print(f"||x̄ - x||{norm_symbol} / || x ||{norm_symbol}")
        print(
            f"Tatsächlicher relativer Fehler bezüglich der {norm_symbol}-Norm: {relativer_fehler}"
        )
        print()

    return relativer_fehler


def geschätzter_absoluter_fehler(A, b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    A_invertiert = np.linalg.inv(A)
    A_invertiert_norm = np.linalg.norm(A_invertiert, norm)
    b_b_tilde_norm = np.linalg.norm(b - b_tilde, norm)

    if debug:
        print("---------- Geschätzter absoluter Fehler ----------")
        print(f"A^-1 \n=\n{A_invertiert}")
        print(f"A^-1 {norm_symbol}-Norm =  {A_invertiert_norm}")
        print(f"b - b_tilde \n=\n{(b - b_tilde).reshape(-1, 1)}")
        print(f"b - b_tilde {norm_symbol}-Norm = {b_b_tilde_norm}")
        print(f"|| x - x~||{norm_symbol} <= ||A^-1||{norm_symbol} * ||b-b~||{norm_symbol}")

    return np.dot(A_invertiert_norm, b_b_tilde_norm)


def geschätzter_relativer_fehler(A, b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    A_konditionszahl = np.linalg.norm(A, norm) * np.linalg.norm(np.linalg.inv(A), norm)
    b_b_tile_norm = np.linalg.norm(b - b_tilde, norm)
    b_norm = np.linalg.norm(b, norm)
    result = A_konditionszahl * (b_b_tile_norm / b_norm)

    if debug:
        print()
        print("---------- Geschätzter relativer Fehler ----------")
        print(f"cond(A) = {A_konditionszahl}")
        print(f"b - b_tilde {norm_symbol}-Norm = {b_b_tile_norm}")
        print(f"b {norm_symbol}-Norm = {b_norm}")
        print(f"||A||{norm_symbol} * ||A^-1||{norm_symbol} * ||b-b~||{norm_symbol} / ||b||{norm_symbol}")
        print()

    return result


def max_epsilon_berechnen(b, max_rel_Fehler, debug=False):
    norm_symbol = convert_norm(norm)
    b_norm = np.linalg.norm(b, norm)
    kondition_A = kondition.matrix_konditionszahl(A, norm)
    epsilon = (max_rel_Fehler / kondition_A) / b_norm

    if debug:
        print("Beweis")
        print(
            f"||x̄ - x||{norm_symbol} / ||x||{norm_symbol} <= cond(A){norm_symbol} * (||b - b_tilde||{norm_symbol} / ||b||{norm_symbol} ) <= {max_rel_Fehler}"
        )
        print(
            f"||x̄ - x||{norm_symbol} / ||x||{norm_symbol} <= {kondition_A} * ε / {b_norm} <= {max_rel_Fehler}"
        )
        print(f"ε <= ({max_rel_Fehler} * {b_norm}) / {kondition_A} \n=\n{epsilon}\n")
        print(
            "ACHTUNG: Wenn ε nicht 1 ist sonder 2ε dann muss Endresultat noch durch zwei geteilt werden!!!\n"
        )
    return epsilon


########################################################################################

# Matrix A definieren
# A = np.array([[2, 4], [4, 8.1]])
# A = np.array([[4, -2], [1, 2]])

# Vektor b definieren
# b = np.array([8, 2])

# Vektor b_tilde definieren

# 2. Wenn b_tilde bekannt ist, kann die Norm mit numpy berechnet werden
# b_tilde = np.array([6, -1])

# Norm definieren (1, 2, np.inf)
norm = np.inf

# tatsächlicher_absoluter_fehler(A, b, b_tilde, norm, True)
# tatsächlicher_relativer_fehler(A, b, b_tilde, norm, True)
# kondition.matrix_konditionszahl(A, norm, True)
# print(f"Geschätzter absoluter Fehler: {geschätzter_absoluter_fehler(A, b, b_tilde, norm, True)}")
# print(f"Geschätzter relativer Fehler: {geschätzter_relativer_fehler(A, b, b_tilde, norm, True)}")

########################################################################################

# Matrix A definieren
A = np.array([[240,120,80], [60,180,170], [60,90,500]])

# Vektor b definieren
b = np.array([3080,4070,5030])

# 1. Wenn b_tilde mit parameter berechnet werden soll, muss Norm von Hand gerechnet werden
ε = sp.symbols("ε")
# b_tilde = np.array([1, 1, ε])
# print(f"Von Hand Norm berechnen von: {b - b_tilde}")

# Norm definieren (1, 2, np.inf)
norm = np.inf

# Maximaler relativer Fehler definieren
max_rel_x_Fehler = 0.01
b_fehler = 1.05
b_tilde = b * b_fehler

# epsilon = max_epsilon_berechnen(b, max_rel_x_Fehler, True)
# b_tilde = np.array([1, 1, epsilon])
# tatsächlicher_absoluter_fehler(A, b, b_tilde, norm, True)
# tatsächlicher_relativer_fehler(A, b, b_tilde, norm, True)
print(
    f"Geschätzter absoluter Fehler: {geschätzter_absoluter_fehler(A, b, b_tilde, norm, True)}"
)
print(
    f"Geschätzter relativer Fehler: {geschätzter_relativer_fehler(A, b, b_tilde, norm, True)}"
)
