import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.05)
f1 = np.exp(x)
plt.figure()
plt.plot(x, f1)
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Aufgabe 2, a")
plt.legend(["e^x"])
plt.show()

x2 = np.arange(-10, 10, 0.1)
f2 = x2**5 + 3 * x2**4 + 3 * x2**2 + x2 + 1
plt.figure()
plt.plot(x2, f2)
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Aufgabe 2, b")
plt.legend(["x^5 + 3x^4 + 3x^2 + x + 1"])
plt.show()

x3 = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
g1 = (1 / 2) * np.sin(3 * x3)
h1 = (1 / 2) * np.cos(3 * x3)
plt.figure()
plt.plot(x3, g1)
plt.plot(x3, h1)
plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Aufgabe 2, c")
plt.legend(["0.5 * sin(3x)", "0.5 * cos(3x)"])
plt.show()
