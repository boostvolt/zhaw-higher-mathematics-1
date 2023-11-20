import numpy.linalg as l
import numpy as np


def serie_9(A, A_tilde, b, b_tilde):
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)

    dx_max = np.nan
    if l.cond(A, np.inf) * (l.norm((A - A_tilde), np.inf) / l.norm(A, np.inf)) < 1:
        dx_max = (
            l.cond(A, np.inf)
            / (
                1
                - l.cond(A, np.inf) * l.norm((A - A_tilde), np.inf) / l.norm(A, np.inf)
            )
        ) * (
            l.norm((A - A_tilde), np.inf) / l.norm(A, np.inf)
            + l.norm((b - b_tilde), np.inf) / l.norm(b, np.inf)
        )

    dx_obs = (l.norm(x - x_tilde, np.inf)) / (l.norm(x, np.inf))

    return (x, x_tilde, dx_max, dx_obs)


A = np.array([[20, 30, 10], [10, 17, 6], [2, 3, 2]])
A_tilde = np.array([[19.9, 29.9, 9.9], [9.9, 16.9, 5.9], [1.9, 2.9, 1.9]])

b = np.array([5720, 3300, 836])
b_tilde = np.array([5820, 3400, 936])

print(serie_9(A, A_tilde, b, b_tilde))
