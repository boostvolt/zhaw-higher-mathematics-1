import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.1, 1.3, 10**-7)
plt.semilogy(
    x, (100 * (x - 1) * x) / (100 * x**2 - 200 * x + 99), label="Kondition h(x)"
)
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
