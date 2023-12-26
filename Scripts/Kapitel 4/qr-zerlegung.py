import math

import numpy as np


def householder(u):
    u = np.array(u)
    if len(u.shape) != 2 or u.shape[1] != 1:
        raise ValueError("u muss ein vertikaler Vektor der Form (n,1) sein")

    u_tilde = u / np.linalg.norm(u)

    return np.identity(u.shape[0]) - 2 * np.matmul(u_tilde, u_tilde.T)


def sign(x):
    return int(math.copysign(1, x))


def a_in_qr_zerlegen(A, debug=False):
    A = np.array(A)
    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(
            "A muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )

    n = A.shape[0]
    R = np.copy(A)
    Q = np.identity(n)

    if debug:
        print("-- A in A =  Q · R zerlegen")

    for i in range(n - 1):
        a = R[i:, i].reshape((n - i, 1))
        e = np.zeros((n - i, 1))
        e[0, 0] = 1
        v = a + sign(a[0, 0]) * np.linalg.norm(a) * e
        u = v / np.linalg.norm(v)
        H = householder(u)
        Q_i = np.identity(n)
        Q_i[i:, i:] = H

        R = np.matmul(Q_i, R)
        Q = np.matmul(Q, Q_i.T)

        if debug:
            print()
            print("---- Iteration {}".format(i + 1))
            print("a_{}:".format(i + 1))
            print(a)
            print("e_{}:".format(i + 1))
            print(e)
            print("v_{}:".format(i + 1))
            print(v)
            print("u_{}:".format(i + 1))
            print(u)
            print("H_{}:".format(i + 1))
            print(H)
            print("Q_{}:".format(i + 1))
            print(Q_i)

    return Q, R


def lgs_nach_x_loesen(Q, R, b, debug=False):
    import numpy as np

    x = np.linalg.solve(R, np.matmul(Q.T, b))

    if debug:
        print()
        print("-- LGS R · x = Q^T · b nach x mit Rückwärtseinsetzen lösen")
        print("Q:")
        print(Q)
        print("R:")
        print(R)
        print("Q^T * b")
        print(np.matmul(Q.T, b))
        print("x:")
        print(x)
        print()

    return x


def qr_zerlegung(A, b, debug=False):
    A = np.array(A)
    b = np.array(b)

    if len(A.shape) != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(
            "A muss eine quadratische Matrix sein, also die Form (n,n) haben."
        )
    if len(b.shape) != 2 or b.shape[1] != 1:
        raise ValueError("b muss ein Vektor der Form (n,1) sein.")
    if A.shape[0] != b.shape[0]:
        raise ValueError("A und b müssen die gleiche Höhe haben")

    Q, R = a_in_qr_zerlegen(A, debug)
    x = lgs_nach_x_loesen(Q, R, b, debug)

    return Q, R, x


A = np.array([[2, 2, -1], [1, -1, 0], [2, 0, 1]])
b = np.array([[-1 / 3], [-11 / 3], [2 / 3]])
qr_zerlegung(A, b, debug=True)
