import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 101)

plt.loglog(x, 5 / ((2 * x**2) ** (1 / 3)), label="f(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.semilogy(x, 10**5 * ((2 * np.e) ** (-x / 100)), label="g(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.semilogy(x, ((625 / 64) ** x), label="h(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
