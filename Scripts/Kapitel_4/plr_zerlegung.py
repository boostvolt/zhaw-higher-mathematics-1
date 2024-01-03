import numpy as np


def a_in_plr_zerlegen(A, debug=False):
    A = np.array(A)
    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(
            "A muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )

    n = len(A)

    L = np.identity(n, dtype="float64")
    R = np.copy(A).astype("float64")
    P = np.identity(n, dtype="short")

    if debug:
        print("-- A in P · A = L · R zerlegen")

    for i in range(n):
        max_value = np.max(np.abs(R[i:, i]))

        for j in range(i + 1, n):
            if np.abs(R[j][i]) == max_value:
                P2 = np.identity(n, dtype="short")
                P2[i][j] = 1
                P2[j][i] = 1
                P2[i][i] = 0
                P2[j][j] = 0
                P = np.matmul(P2, P)
                R = np.matmul(P2, R)

                if debug:
                    print()
                    print("---- Nächster Schritt")
                    print(
                        "------ Zeile {} mit Zeile {} tauschen (P, R)".format(
                            i + 1, j + 1
                        )
                    )
                    print("P:")
                    print(P)
                    print("R:")
                    print(R)
                    print("L:")
                    print(L)
                break

        for j in range(i + 1, n):
            factor = R[j][i] / R[i][i]
            L[j][i] = factor
            R[j] = R[j] - factor * R[i]

            if debug:
                print()
                print("---- Nächster Schritt")
                print(
                    "------ Zeile {} minus {} · Zeile {} (R)".format(
                        j + 1, round(factor, 3), i + 1
                    )
                )
                print("P:")
                print(P)
                print("R:")
                print(R)
                print("L:")
                print(L)

    if debug:
        print()
        print("---- Abgeschlossene Zerlegung")
        print("P:")
        print(P)
        print("R:")
        print(R)
        print("L:")
        print(L)
        print("--")
        print()

    return [L, R, P]


def lgs_nach_y_loesen(L, P, b, debug=False):
    L = np.array(L)
    P = np.array(P)
    b = np.array(b)
    if len(L.shape) != 2 or L.shape[0] != L.shape[1]:
        raise ValueError(
            "L muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )
    if len(P.shape) != 2 or P.shape[0] != P.shape[1]:
        raise ValueError(
            "P muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )
    if len(b.shape) != 2 or b.shape[1] != 1:
        raise ValueError("b muss ein Vektor der Form (n,1) sein.")
    if P.shape[0] != L.shape[0] or P.shape[0] != b.shape[0]:
        raise ValueError("L, P und b müssen die gleiche Höhe haben.")

    n = len(L)
    P_b = np.matmul(P, b)
    y = np.zeros((n, 1))

    if debug:
        print("-- LGS L · y = P · b nach y mit Vorwärtseinsetzen lösen")

    for i in range(n):
        y[i] = P_b[i] - np.sum(L[i] * y.T)

    if debug:
        print("y:")
        print(y)
        print("--")
        print()

    return y


def lgs_nach_x_loesen(R, y, debug=False):
    R = np.array(R)
    y = np.array(y)
    if len(R.shape) != 2 or R.shape[0] != R.shape[1]:
        raise ValueError(
            "R muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )
    if len(y.shape) != 2 or y.shape[1] != 1:
        raise ValueError("y muss ein Vektor der Form (n,1) sein.")
    if R.shape[0] != b.shape[0]:
        raise ValueError("R und y müssen die gleiche Höhe haben.")

    n = len(R)

    if debug:
        print("-- LGS R · x = y nach x mit Rückwärtseinsetzen lösen")

    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(R[i] * x.T)) / R[i][i]

    if debug:
        print("x:")
        print(x)
        print("--")
        print()

    return x


def plr_zerlegung(A, b, debug=False):
    L, R, P = a_in_plr_zerlegen(A, debug)
    y = lgs_nach_y_loesen(L, P, b, debug)
    return lgs_nach_x_loesen(R, y, debug)


########################################################################################

# Matrix a definieren
A = np.array([[2, 1, 0], [4, 0, -1], [2, 3, -1]])

# Vektor b definieren
b = np.array([[4], [1], [5]])

plr_zerlegung(A, b, True)
