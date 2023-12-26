import numpy as np
import numpy.linalg as lin


def serie_9(A, A_tilde, b, b_tilde):
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    relA = lin.norm((A - A_tilde), np.inf) / lin.norm(A, np.inf)
    condARel = lin.cond(A, np.inf) / (1 - lin.cond(A, np.inf) * relA)
    bRel = lin.norm((b - b_tilde), np.inf) / lin.norm(b, np.inf)
    xRel = (lin.norm(x - x_tilde, np.inf)) / (lin.norm(x, np.inf))

    dx_max = np.nan

    if (
        lin.cond(A, np.inf) * (lin.norm((A - A_tilde), np.inf) / lin.norm(A, np.inf))
        < 1
    ):
        dx_max = condARel * (relA + bRel)

    dx_obs = xRel

    return (x, x_tilde, dx_max, dx_obs)


A = np.array([[20, 30, 10], [10, 17, 6], [2, 3, 2]])
A_tilde = np.array([[19.9, 29.9, 9.9], [9.9, 16.9, 5.9], [1.9, 2.9, 1.9]])

b = np.array([5720, 3300, 836])
b_tilde = np.array([5820, 3400, 936])

print(serie_9(A, A_tilde, b, b_tilde))

# Die mit Python berechneten Resultate stimmen mit den Resultaten aus Aufgabe 3 der Serie 8 überein.
