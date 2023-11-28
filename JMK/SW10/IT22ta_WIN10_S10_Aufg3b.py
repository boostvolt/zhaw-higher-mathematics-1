import numpy.linalg as l
import numpy as np
import matplotlib.pyplot as plt
import timeit
from IT22ta_WIN10_S6_Aufg2 import solve_linalg_sys
from IT22ta_WIN10_S10_Aufg3a import aufgabe_3_a

dim = 3000
A = np.diag(np.diag(np.ones((dim, dim)) * 4000)) + np.ones((dim, dim))
dum_1 = np.arange(1, int(dim / 2 + 1), dtype=np.float64).reshape((int(dim / 2), 1))
dum_2 = np.arange(int(dim / 2), 0, -1, dtype=np.float64).reshape((int(dim / 2), 1))
x = np.append(dum_1, dum_2, axis=0)
b = A @ x
x_0 = np.zeros((dim, 1))
tol = 1e-4

# Jacobi
start = timeit.default_timer()
#jacobi_result = aufgabe_3_a(A, b, x_0, tol)
end = timeit.default_timer()
print(f"Jacobi: {end - start} s")
# 142.94855400000233 s

# Gauss-Seidel
start = timeit.default_timer()
#gauss_seidel_result = aufgabe_3_a(A, b, x_0, tol, "gauss-seidel")
end = timeit.default_timer()
print(f"Gauss-Seidel: {end - start} s")
# 83.91509779200715 s

# Gaussian
start = timeit.default_timer()
gaussian_result = solve_linalg_sys(A, b) #TODO: fix overflow
end = timeit.default_timer()
print(f"Gaussian: {end - start} s")

# l.solve
start = timeit.default_timer()
#l.solve(A, b)
end = timeit.default_timer()
print(f"l.solve: {end - start} s")
# 0.21959929099830333 s

plt.figure()
# plt.plot(np.abs(gaussian_result - x), label="Gauss")  # TODO: Fix overflow
# plt.plot(np.abs(jacobi_result[0] - x), label="Jacobi")
# plt.plot(np.abs(gauss_seidel_result[0] - x), label="Gauss-Seidel")
plt.legend()
plt.xlabel("Vector Element")
plt.ylabel("Absolute Error")
plt.title("Absolute Error for Each Vector Element")
plt.show()
