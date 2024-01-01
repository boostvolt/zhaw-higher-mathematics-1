import numpy as np
import sympy as sp


def eigenwert(A):
    A = np.matrix(A)
    eigenwerte = np.linalg.eigvals(A)
    print(f"Eigenwerte von A: {eigenwerte}")
    return eigenwerte


def eigenvektor(A):
    A = sp.matrices.Matrix(A)

    data = A.eigenvects()
    for idx, values in enumerate(data):
        vec = str(values[2])
        print(
            f"\nEigenvektor(en) zu Eigenwert {values[0]}: \n{vec}\n".replace(
                "Matrix", ""
            )
        )


def charakteristisches_polynom(A):
    A = sp.matrices.Matrix(A)

    λ = sp.symbols("λ")
    E = sp.matrices.eye(A.shape[0])
    polynom = A.charpoly().as_expr()
    factorized_polynom = sp.factor(polynom)
    print(f"det(A - λI) = det({A - λ * E})")
    try:
        print(f"Polynom p(x) = {polynom} = {factorized_polynom}".replace("lambda", "λ"))
    except:  # noqa: E722
        print(f"Polynom p(x) = {polynom} = {factorized_polynom}")

    return polynom, factorized_polynom


def berechne_eigenwert_mit_charakteristischem_polynom(A):
    polynom, factorized_polynom = charakteristisches_polynom(A)
    lambda_aka_eigenwerte = sp.solvers.solve(polynom, sp.symbols("lambda"))
    try:
        expr = [
            f"({i + 1}) λ = {lambda_aka_eigenwerte[i]}, "
            for i in range(len(lambda_aka_eigenwerte))
        ]
        expr = "".join(expr)
        expr = expr.removesuffix(", ")
        print(f"{expr}")
    except:  # noqa: E722
        print("λ = ", lambda_aka_eigenwerte)
    print("=> Eigenwerte = ", lambda_aka_eigenwerte)


def ev_zum_ew(A, eigenwert):
    b = np.zeros(A.shape[0])
    A_new = A - eigenwert * np.eye(A.shape[0])
    R = a_in_obere_dreicksmatrix(A_new, True)
    geometrische_vielfachheit(R, eigenwert)
    try:
        # Solve the system of equations
        solution = np.linalg.solve(A_new, b)
        print("Solution:")
        print(solution)
    except np.linalg.LinAlgError:  # Wenn es unendlich viele Lösungen gibt
        ev_zum_ew_parametrisiert(A, eigenwert)


def ev_zum_ew_parametrisiert(A, eigenwert):
    A = sp.Matrix(A - eigenwert * np.eye(A.shape[0]))
    b = sp.Matrix(np.zeros(A.shape[0]))

    # Hier Anzahl freie Variablen anpassen
    solution = sp.linsolve((A, b), sp.symbols("x y z"))

    print(f"Parametrisierte Lösung: {solution}")


def ev_zum_ew_komplexe_Zahl(A):
    b = sp.Matrix(np.zeros_like(A))

    # Hier Anzahl freie Variablen anpassen
    solution = sp.linsolve((A, b), sp.symbols("x y"))

    print(f"Parametrisierte Lösung: {solution}")


def a_in_obere_dreicksmatrix(A):
    A = np.array(A)
    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(
            "A muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )

    n = len(A)

    L = np.identity(n, dtype="float64")
    R = np.copy(A).astype("float64")

    print("-- A in eine obere Dreickesmatrix zerlegen (R)")

    for i in range(n):
        for j in range(i + 1, n):
            if R[j][i] != 0:
                print("---- Nächster Schritt")
                print(R)
                print(f"Zeile {j + 1} - ({R[j][i]}/{R[i][i]}) · Zeile {i + 1}")

                factor = R[j][i] / R[i][i]
                L[j][i] = factor
                R[j] = R[j] - factor * R[i]
                print(R)
    print("---- Abgeschlossene Zerlegung")
    print(f"R: \n{R}")
    return R


def geometrische_vielfachheit(R):
    print(
        f"Geometrische Vielfachheit = n - Rg(A - λI) = {R.shape[0]} - {np.linalg.matrix_rank(R)} = {R.shape[0] - np.linalg.matrix_rank(R)}"
    )


# A = np.array([[0, -1], [1, 0]])
# A = np.array([[2, 5], [-1, -2]])
A = np.array([[0, 1, 1], [1, 0, 1], [1, 1, 0]])

berechne_eigenwert_mit_charakteristischem_polynom(A)

# Wenn Eigenwert keine komplexe Zahl ist
# ev_zum_ew(A, -1)

# Wenn Eigenwert eine komplexe Zahl ist, dann manuell die diagonale Matrix mit der komplexen Zahl subtrahieren
# A = sp.Matrix([[2 - 1j, 5], [-1, -2 - 1j]])
# ev_zum_ew_komplexe_Zahl(A)

# Wichtig! Eigenraum selber von Eigenvektoren ablesen, parametrisierte Lösung kann momentan nicht weiterverarbeitet werden um den Raum zu bestimmen

# Zur Überprüfung der Eigenwerte
eigenwert(A)

# Zur Überprüfung der Eigenvektoren
eigenvektor(A)
