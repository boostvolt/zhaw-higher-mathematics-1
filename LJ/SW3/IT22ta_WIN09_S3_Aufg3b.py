import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
fx = 5 / ((2*x**2)** (1/3))
plt.loglog(x, fx)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Koordinatensystem mit logarhitmischer x- und y-Achse')
plt.legend(['f(x)'])
plt.xlim(0, 100)
plt.grid()
plt.show()

x = np.arange(0, 100)
gx = 10 ** 5 * ((2 * np.e) ** ((-x) / 100))
plt.semilogy(x, gx)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Koordinatensystem mit logarhitmischer y-Achse')
plt.legend(['g(x)'])
plt.xlim(0, 100)
plt.grid()
plt.show()

x = np.arange(0, 100)
hx = (625 / 64) ** x
plt.semilogy(x, hx)

plt.xlabel('x')
plt.ylabel('y axis')
plt.title('Koordinatensystem mit logarhitmischer y-Achse')
plt.legend(['h(x)'])
plt.grid()
plt.show()