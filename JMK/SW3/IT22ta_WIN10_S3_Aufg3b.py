import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(0, 101)
plt.loglog(x, 5 / ((2 * x**2) ** (1 / 3)), label="f(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

x = np.arange(1, 101)
plt.semilogy(x, 10**5 * ((2 * np.e) ** (-x / 100)), label="g(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

x = np.logspace(0, 101)
plt.semilogx(x, ((10 ** (2 * x)) / (2 ** (5 * x))) ** 2, label="h(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
