import matrix_konditionszahl as cond
import numpy as np
import sympy as sp


def convert_norm(norm):
    if norm == np.inf:
        return "∞"
    else:
        return f"_{norm}"


def berechne_x(A, b, debug=False):
    x = np.linalg.solve(A, b)
    if debug:
        print(f"A = \n {A}")
        print(f"b = \n {b}")
        print(f"x = \n {x}")
        print()
    return x


def berechne_x_tilde(A_tilde, b_tilde, debug=False):
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    if debug:
        print(f"A_tilde = \n {A_tilde}")
        print(f"b_tilde = \n {b_tilde}")
        print(f"x_tilde = \n {x_tilde}")
        print()
    return x_tilde


def berechne_epsilon_mit_geschätztem_relativen_fehler(
    A, A_tilde, rel_x_fehler, b, debug=False
):
    A_minus_A_tilde_norm = np.linalg.norm(A - A_tilde, norm)
    b_norm = np.linalg.norm(b, norm)
    A_norm = np.linalg.norm(A, norm)

    print("Ist relativer Fehler begrenzt?")
    cond_A = cond.matrix_konditionszahl(A, norm)
    relativer_fehler = cond_A * A_relativer_fehler(A, A_tilde, norm)

    # Fehlerabschätzungsbedingung
    if relativer_fehler < 1:
        epsilon = (
            (rel_x_fehler * (1 - relativer_fehler) / cond_A)
            - (A_minus_A_tilde_norm / A_norm)
        ) * b_norm
        if debug:
            print("cond(A)∞ * (|||A - Ã||∞ / ||A||∞) < 1")
            print(
                f"{cond_A} * ({A_minus_A_tilde_norm} / {A_norm} = {relativer_fehler}) < 1"
            )
            print("Relativer Fehler in x ist begrenzt")
            print("")
            print(
                "||x - x̄||∞ / ||x||∞ <= cond(A)∞ / (1 - cond(A)∞ * (||A - Ã||∞ / ||A||∞)) * (||A - Ã||∞ / ||A||∞  +  ||b - ᵬ||∞ / ||b||∞) "
            )
            print(
                f"{cond_A} / (1 - {cond_A} * {A_tilde}) * (({A_tilde} / {A_norm}) + (ε / {b_norm})) <= 1"
            )
            print(f"Epsilon: {epsilon}")

    else:
        print("Relativer Fehler in x ist NICHT begrenzt")
    return epsilon


def geschätzter_relativer_x_fehler(A, A_tilde, b, b_tilde, norm, debug=False):
    print("Ist relativer Fehler begrenzt?")
    cond_A = cond.matrix_konditionszahl(A, norm)
    A_rel_fehler = A_relativer_fehler(A, A_tilde, norm)
    b_rel_fehler = b_relativer_fehler(b, b_tilde, norm)
    relativer_fehler = cond_A * A_rel_fehler

    print("Fehlerabschätzungsbedingung: cond(A)∞ * (|||A - Ã||∞ / ||A||∞) < 1")
    print(f"{cond_A} * {A_rel_fehler} = {relativer_fehler} < 1")
    # Fehlerabschätzungsbedingung
    if relativer_fehler < 1:
        geschätzter_fehler = (cond_A / (1 - relativer_fehler)) * (
            A_rel_fehler + b_rel_fehler
        )
        if debug:
            print("")
            print("Relativer Fehler in x ist begrenzt")
            print("")
            print(
                "||x - x̄||∞ / ||x||∞ <= cond(A)∞ / (1 - cond(A)∞ * (||A - Ã||∞ / ||A||∞)) * (||A - Ã||∞ / ||A||∞  +  ||b - ᵬ||∞ / ||b||∞) "
            )
            print(
                f"({cond_A} / (1 - {cond_A} * {relativer_fehler})) * ({A_rel_fehler} + {b_rel_fehler})"
            )
            print(f"Geschätzter relativer Fehler: {geschätzter_fehler}")

    else:
        print("Relativer Fehler in x ist NICHT begrenzt")


def A_relativer_fehler(A, A_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    A_norm = np.linalg.norm(A, norm)
    A_tilde_A_norm = np.linalg.norm(A - A_tilde, norm)
    A_relativer_fehler = A_tilde_A_norm / A_norm

    if debug:
        print(f"A = \n {A}\n")
        print(f"Ã = \n {A_tilde}\n")
        print(
            f"Relativer Fehler in A: ||A - Ã||{norm_symbol} / ||A||{norm_symbol} = \n"
        )
        print(f"||{A - A_tilde}||{norm_symbol} \n/\n||{A}||{norm_symbol}\n=")
        print(f"{A_relativer_fehler}\n")
    return A_relativer_fehler


def b_relativer_fehler(b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    b_norm = np.linalg.norm(b, norm)
    b_tilde_b_norm = np.linalg.norm(b_tilde - b, norm)
    b_relativer_fehler = b_tilde_b_norm / b_norm

    if debug:
        print(f"b = \n {b}\n")
        print(f"b̄ = \n {b_tilde}\n")
        print(f"Relativer Fehler in b: ||b - b̄||{norm_symbol} / ||b||{norm_symbol}\n")
        print(f"||{b - b_tilde}||{norm_symbol} \n/\n||{b}||{norm_symbol}\n=")
        print(f"{b_relativer_fehler}\n")
    return b_relativer_fehler


def x_relativer_fehler(x, x_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    x_norm = np.linalg.norm(x, norm)
    x_tilde_x_norm = np.linalg.norm(x_tilde - x, norm)
    x_relativer_fehler = x_tilde_x_norm / x_norm

    if debug:
        print(f"x = \n {x}\n")
        print(f"x̄ = \n {x_tilde}\n")
        print(f"Relativer Fehler in x: ||x - x̄||{norm_symbol} / ||x||{norm_symbol}\n")
        print(f"||{x - x_tilde}||{norm_symbol} \n/\n||{x}||{norm_symbol}\n=")
        print(f"{x_relativer_fehler}\n")
    return x_relativer_fehler


def tatsächlicher_absoluter_fehler(A, A_tilde, b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    x = berechne_x(A, b, True)
    x_tilde = berechne_x_tilde(A_tilde, b_tilde, True)
    x_minus_x_tilde = x - x_tilde
    absoluter_fehler = np.linalg.norm(x_minus_x_tilde, norm)

    if debug:
        print(f"x = {x}")
        print(f"x̄ = {x_tilde}")
        print(f"||x̄ - x||{norm_symbol} \n=\n{x_minus_x_tilde}")
        print(
            f"Tatsächlicher absoluter Fehler bezüglich der {norm_symbol}-Norm: {absoluter_fehler}"
        )
        print()

    return absoluter_fehler


def tatsächlicher_relativer_fehler(A, A_tilde, b, b_tilde, norm, debug=False):
    norm_symbol = convert_norm(norm)
    x = berechne_x(A, b)
    x_tilde = berechne_x_tilde(A_tilde, b_tilde)
    x_minus_x_tilde = x - x_tilde
    x_minus_x_tilde_norm = np.linalg.norm(x_minus_x_tilde, norm)
    x_norm = np.linalg.norm(x, norm)
    relativer_fehler = x_minus_x_tilde_norm / x_norm

    if debug:
        print(f"x = {x}")
        print(f"x̄ = {x_tilde}")
        print(f"||x̄ - x||{norm_symbol} \n=\n{x_minus_x_tilde}")
        print(f"||x||{norm_symbol} = {x_norm}")
        print(
            f"Tatsächlicher relativer Fehler bezüglich der {norm_symbol}-Norm: {relativer_fehler}"
        )
        print()

    return relativer_fehler


########################################################################################
# Diese Funktion hier benutzen, wenn b_tilde gegeben ist

# # Matrix A und A_tilde definieren
# A = np.array([[1/2, -1/2], [1/6, 1/3]])

# # 1. Option wenn A und Störung von A bekannt
# störung = 10**(-7)
# A_tilde = A + störung

# # 2. Option wenn A_tilde bekannt ist
# A_tilde = np.array([[0.5, -0.5], [0.2, 0.3]])

# # Vektor b definieren
# b = np.array([1, -1/6])
# b_tilde = np.array([1, -0.2])

# # Norm definieren (1, 2, np.inf)
# norm = 1

# A_relativer_fehler(A, A_tilde, norm, True)
# b_relativer_fehler(b, b_tilde, norm, True)
# x_relativer_fehler(berechne_x(A, b), berechne_x_tilde(A_tilde, b_tilde), norm, True)
# geschätzter_relativer_x_fehler(A, A_tilde, b, b_tilde, True)

########################################################################################
# Diese Funktion hier benutzen, wenn b_tilde mit Parameter berechnet werden soll

# Norm definieren (1, 2, np.inf)
norm = np.inf

# Maximaler relativer Fehler definieren
max_rel_x_Fehler = 0.01

# Matrix A definieren
A = np.array([[1, 0, 2], [0, 1, 0], [10 ** (-4), 0, 10 ** (-4)]])

# # 1. Option wenn A und Störung von A bekannt
störung = 10 ** (-7)
A_tilde = A + störung

# # 2. Option wenn A_tilde bekannt ist
# # A_tilde = np.array([[0.5, -0.5], [0.2, 0.3]])

# Vektor b definieren
b = np.array([1, 1, 0])

# 1. Wenn b_tilde mit parameter berechnet werden soll, muss Norm von Hand gerechnet werden
ε = sp.symbols("ε")
b_tilde = np.array([1, 1, ε])
print(f"Von Hand Norm berechnen von: {b - b_tilde}")

epsilon = berechne_epsilon_mit_geschätztem_relativen_fehler(
    A, A_tilde, max_rel_x_Fehler, b, True
)
b_tilde = np.array([1, 1, epsilon])
tatsächlicher_absoluter_fehler(A, A_tilde, b, b_tilde, norm, True)
tatsächlicher_relativer_fehler(A, A_tilde, b, b_tilde, norm, True)
geschätzter_relativer_x_fehler(A, A_tilde, b, b_tilde, norm, True)
