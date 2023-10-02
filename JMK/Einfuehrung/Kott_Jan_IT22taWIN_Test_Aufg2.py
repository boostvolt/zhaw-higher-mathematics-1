import numpy as np
import matplotlib.pyplot as plt

# Abbildung 1
x = np.arange(-5, 5, 0.05)
f = np.exp(x)
plt.figure()
plt.plot(x, f)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Abbildung 1")
plt.legend(["e^x"])
plt.show()

# Abbildung 2
x2 = np.arange(-10, 10, 0.1)
f2 = x2**5 + 3 * x2**4 + 3 * x2**2 + x2 + 1
plt.figure()
plt.plot(x2, f2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Abbildung 2")
plt.legend(["x^5 + 3x^4 + 3x^2 + x + 1"])
plt.show()

# Abbildung 3
x3 = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
g = (1 / 2) * np.sin(3 * x3)
h = (1 / 2) * np.cos(3 * x3)
plt.figure()
plt.plot(x3, g)
plt.plot(x3, h)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Abbildung 3")
plt.legend(["0.5 * sin(3x)", "0.5 * cos(3x)"])
plt.show()
