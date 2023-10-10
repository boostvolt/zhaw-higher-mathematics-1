import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2.0, 0.1)
plt.plot(x, np.sqrt((100 * (x**2)) - (200 * x) + 99), label="f(x)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0.75, 1.25)
plt.show()

x = 0.8
print(np.sqrt(100 * (x**2) - 200 * x + 99))

x = 1.2
print(np.sqrt(100 * (x**2) - 200 * x + 99))

x = 1.1
print(np.sqrt(100 * (x**2) - 200 * x + 99))

# Aufgabe 4b)
x = np.logspace(np.log10(1.1), np.log10(1.3), 200)
cond = np.abs(x * (100 * (x - 100)) / (2 * np.sqrt(100 * (x**2) - 200 * x + 99) ** 2))
plt.semilogx(x, cond)
plt.xlabel("x")
plt.ylabel("Kondition von h(x)")
plt.show()
