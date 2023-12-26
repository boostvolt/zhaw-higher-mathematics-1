import matplotlib.pyplot as plt
import numpy as np
from IT22ta_WIN09_S10_Aufg3a import IT22ta_WIN09_S10_Aufg3a
from sympy import false, true

# Aufgabe 3b
dim = 3000
A = np.diag(np.diag(np.ones((dim, dim)) * 4000)) + np.ones((dim, dim))
print(A)
dum1 = np.arange(1, int(dim / 2 + 1), dtype=np.float64).reshape((int(dim / 2), 1))
dum2 = np.arange(int(dim / 2), 0, -1, dtype=np.float64).reshape((int(dim / 2), 1))
x = np.append(dum1, dum2, axis=0)
b = A @ x
x0 = np.zeros((dim, 1))
tol = 1e-4
opt = true

# Linalg.solve() Laufzeit
# t1 = timeit.timeit(lambda: np.linalg.solve(A, b), number=1)
# #Jacobi Laufzeit
# t2 = timeit.timeit(lambda: IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, opt), number=1)
# #Gauss-Seidel Laufzeit
# opt = false
# t3 = timeit.timeit(lambda: IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, opt), number=1)
# #Gauss Laufzeit
# t4 = timeit.timeit(lambda: obereDreiecksMatrix(A, b), number=1)

# print("Linagl.solve() Laufzeit: {}".format(t1))
# print("Jacobi-Laufzeit: {}".format(t2))
# print("Gauss-Seidel Laufzeit: {}".format(t3))
# print("Gauss-Zerlegung Laufzeit: {}".format(t4))
# print("Gauss braucht {} mal länger als die Gauss-Seidel-Funktion".format(t4/t3))
# Linagl.solve() Laufzeit: 0.21742208395153284
# Jacobi-Laufzeit: 22.236404209048487
# Gauss-Seidel Laufzeit: 5.150750666973181
# Gauss-Zerlegung Laufzeit: 28.33560229104478
# Gauss braucht 5.5012568309186065 mal länger als die Gauss-Seidel-Funktion
# Jedoch bricht unsere Gauss-Funktion schon nach 28 Sekunden ab aufgrund eines Overflows.
# In Realität würde unsere Funktion daher noch deutlich länger benötigen als die eben berechnete Zeit.

# Aufgabe 3c
[xJacobi, _, _] = IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, true)
[xGaussSeidel, _, _] = IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, false)
plt.figure()
plt.plot(np.abs(xJacobi - x), label="Jacobi")
plt.plot(np.abs(xGaussSeidel - x), label="Gauss-Seidel")
plt.legend()
plt.xlabel("Vektor-Element")
plt.ylabel("Absoluter Fehler")
plt.title("Absoluter Fehler pro Vektorelement")
plt.grid()
plt.show()

# Die Jacobi Funktion hat konstant einen absoluten Fehler von ungefähr 4.1 * 10^-5
# Die Gauss-Seidel Funktion schwankt stark zwischen 7.8 * 10^-6 und 0.
# Das heisst die Gauss-Seidel Funktion berechnet das Ergebnis genauer als die Jacobi-Funktion.
