# This is a Python File

import numpy as np
import matplotlib.pyplot as plt
from IT22ta_WIN10_S6_Aufg2 import gaussian_algorithm

# Aufgabe 3a)
A = np.array(
    [
        [0, 0, 0, 1],
        [2**3, 2**2, 2, 1],
        [9**3, 9**2, 9, 1],
        [13**3, 13**2, 13, 1],
    ]
)
b = np.array([150, 104, 172, 152])

x = np.arange(0, 13, 0.1)
plt.figure()
plt.plot(x, np.polyval(gaussian_algorithm(A, b)[2], x))
plt.ylim(90, 190, 1)
plt.grid()
plt.show()

# Aufgabe 3b) Jahr 2003: 126.6 und Jahr 2004: 143.1

# Aufgabe 3c)
x = np.arange(0, 13, 0.1)
y = np.array([150, 104, 172, 152])
coeff = np.polyfit(np.array([0, 2, 9, 13]), y, 3)
plt.figure()
plt.plot(x, np.polyval(coeff, x))
plt.grid()
plt.show()

# Grafisch sieht es identisch aus und mit polyfit bekommen wir diese folgende Werte:
# Jahr 2003: 126.69 und Jahr 2004: 143.03
