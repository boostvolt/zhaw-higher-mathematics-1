import numpy as np


def a_in_lr_zerlegen(A, debug=False):
    A = np.array(A)
    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(
            "A muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )

    n = len(A)

    L = np.identity(n, dtype="float64")
    R = np.copy(A).astype("float64")

    if debug:
        print("-- A = L · R zerlegen")

    for i in range(n):
        for j in range(i + 1, n):
            if R[j][i] != 0:
                if debug:
                    print("---- Nächster Schritt")
                    print(R)
                    print(f"Zeile {j + 1} - ({R[j][i]}/{R[i][i]}) · Zeile {i + 1}")

                factor = R[j][i] / R[i][i]
                L[j][i] = factor
                R[j] = R[j] - factor * R[i]

                if debug:
                    print(R)

    if debug:
        print()
        print("---- Abgeschlossene Zerlegung")
        print("R:")
        print(R)
        print("L:")
        print(L)
        print("--")
        print()

    return [L, R]


def lgs_nach_y_loesen(L, b, debug=False):
    L = np.array(L)
    b = np.array(b)
    if len(L.shape) != 2 or L.shape[0] != L.shape[1]:
        raise ValueError(
            "L muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )
    if len(b.shape) != 2 or b.shape[1] != 1:
        raise ValueError("b muss ein Vektor der Form (n,1) sein.")
    if L.shape[0] != b.shape[0]:
        raise ValueError("L und b müssen die gleiche Höhe haben.")

    n = len(L)
    y = np.zeros((n, 1))

    if debug:
        print("-- LGS L · y = b nach y mit Vorwärtseinsetzen lösen")

    for i in range(n):
        if debug:
            if i == 0:
                print(f"y1 = {b[i]}")
            else:
                print(
                    f"y{i + 1} = ({b[i]} - {y[i - 1]}) / {L[i][i]} = {b[i] - np.sum(L[i] * y.T)}"
                )

        y[i] = b[i] - np.sum(L[i] * y.T)

    if debug:
        print(f"y = \n {y}")
        print("--")
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
        print("Hier Zwischenschritt aufschreiben -> x3 = .., x2 = .., x1 = ..")

    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(R[i] * x.T)) / R[i][i]

    if debug:
        print(f"x: \n{x}")

    return x


def auflösen_nach_x(L, R, b, debug=False):
    y = lgs_nach_y_loesen(L, b, debug)
    return lgs_nach_x_loesen(R, y, debug)


A = np.array([[20, 30, 10], [10, 17, 6], [2, 3, 2]])
b = np.array([[5200], [3000], [760]])
b_neu = np.array([[5720], [3300], [836]])

L, R = a_in_lr_zerlegen(A, True)
y = lgs_nach_y_loesen(L, b, True)
x = lgs_nach_x_loesen(R, y, True)
# Bei neuem B kann das gleiche L und R verwendet werden von vorher
y = lgs_nach_y_loesen(L, b_neu, True)
x = lgs_nach_x_loesen(R, y, True)