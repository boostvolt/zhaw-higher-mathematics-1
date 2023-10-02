import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1.99, 2.01, 501)
f1 = (x ** 7) - (14 * (x ** 6)) + (84 * (x ** 5)) - (280 * (x ** 4)) + (560 * (x ** 3)) - (672 * (x ** 2)) + 448 * x - 128
f2 = (x - 2) ** 7

plt.plot(x, f1)
plt.plot(x, f2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Polynomial')
plt.legend(['f1(x)', 'f2(x)'])
plt.grid()
plt.show()
