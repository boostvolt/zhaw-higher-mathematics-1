import numpy.linalg as l
import numpy as np


def serie_9(A, A_tilde, b, b_tilde):
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)

    dx_max = (
        l.cond(A, np.inf)
        / (1 - l.cond(A, np.inf) * l.norm((A - A_tilde), np.inf) / l.norm(A, np.inf))
    ) * (
        l.norm((A - A_tilde), np.inf) / l.norm(A, np.inf)
        + l.norm((b - b_tilde), np.inf) / l.norm(b, np.inf)
    )

    dx_obs = (l.norm(x, np.inf) - l.norm(x_tilde, np.inf)) / (l.norm(x, np.inf))

    return (x, x_tilde, dx_max, dx_obs)

print()