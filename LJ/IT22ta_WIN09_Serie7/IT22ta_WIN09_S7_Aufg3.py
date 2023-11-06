import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from IT22ta_WIN09_S6_Aufg2 import obereDreiecksMatrix

# Aufgabe 3 
# a)

A = np.array([[0, 0, 0, 1], [8, 4, 2, 1], [729, 81, 9, 1], [2197, 169, 13, 1]])
b = np.array([150, 104, 172, 152])
x1 = np.arange(0, 13, 0.1)

[triangle, det, x] = obereDreiecksMatrix(A,b)
plt.plot(x1 + 1997, np.polyval(x, x1))
plt.xlabel('Jahre')
plt.ylabel('Tage')
plt.title('Aufgabe 3b')
plt.grid()
plt.show()

# b)
# Für 2003 wird ein Wert von 126 Tage geschätzt.
# Für 2004 wird ein Wert von 143 Tage geschätzt.

# c)
# Für 2003 wird ein Wert von 126 Tage geschätzt.
# Für 2004 wird ein Wert von 143 Tage geschätzt.

x2 = np.arange(1997, 2011, 0.1)
x3 = np.polyfit(np.array([1997, 1999, 2006, 2010]), np.array([150, 104, 172, 152]), 3)

print(x1)
plt.plot(x1 + 1997, np.polyval(x, x1))
plt.plot(x2, np.polyval(x3, x2))
plt.xlabel('Jahr')
plt.ylabel('Tage')
plt.title('Aufgabe 3c')
plt.legend(['3b', '3c'])
plt.grid()
plt.show()