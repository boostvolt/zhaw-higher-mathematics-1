import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 4 b)

x = np.arange(1.1, 1.3, 10 ** -7)
h = (100 * (x -1) * x) / (100 * x ** 2 - 200 * x +99)
plt.semilogy(x, h)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Konditionszahl')
plt.legend(['f(x)'])
plt.grid()
plt.show()