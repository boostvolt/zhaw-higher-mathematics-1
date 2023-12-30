import numpy as np
import numpy.linalg as lin

toleranz = 10**(-4)
A = np.array([[8, 5, 2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])

# Jacobi
# B = -lin.inv(D).dot(L+R)