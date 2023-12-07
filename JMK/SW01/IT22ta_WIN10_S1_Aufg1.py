import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
f = (x**5) - (5 * (x**4)) - (30 * (x**3)) + (110 * (x**2)) + (29 * x) - 105
f_deriv = (5 * x**4) - (20 * x**3) - 90 * x**2 + 220 * x + 29
f_integ = (
    (1 / 6) * x**6
    - x**5
    - (30 / 4) * x**4
    + (110 / 3) * x**3
    + (29 / 2) * x**2
    - 105 * x
)

plt.plot(x, f)
plt.plot(x, f_deriv)
plt.plot(x, f_integ)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.xlim(-7.5, 7.5, 0.5)
plt.ylim(-250, 250, 1)
plt.title("Polynomial")
plt.legend(["f(x)", "f_deriv", "f_integral"])
plt.grid()
plt.show()
