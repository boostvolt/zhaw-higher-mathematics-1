import matplotlib.pyplot as plt
import numpy as np
from IT22ta_WIN09_S9_Aufg2 import serie_9

rng = np.random.default_rng(42)


def random_iteration():
    A = rng.random((100, 100))
    A_tilde = A + rng.random((100, 100)) / 10**5

    b = rng.random((100, 1))
    b_tilde = b + rng.random((100, 1)) / 10**5

    _, _, dx_max, dx_obs = serie_9(A, A_tilde, b, b_tilde)

    return dx_max, dx_obs


dx_max_list = []
dx_obs_list = []
ratio_list = []

for _ in range(1000):
    dx_max, dx_obs = random_iteration()
    dx_max_list.append(dx_max)
    dx_obs_list.append(dx_obs)
    ratio_list.append(dx_max / dx_obs)

x = np.arange(1, 1001)
plt.figure()
plt.semilogy(x, dx_max_list, label="dx_max")
plt.semilogy(x, dx_obs_list, label="dx_obs")
plt.semilogy(x, ratio_list, label="ratio")
plt.legend()
plt.grid()
plt.show()

# Ja, dx_max ist eine realistische obere Schranke für dx_obs. Weil dx_obs nie grösser als dx_max ist.
