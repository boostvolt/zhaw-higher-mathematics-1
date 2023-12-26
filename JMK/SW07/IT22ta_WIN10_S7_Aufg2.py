import numpy as np
import scipy as sp

A = np.array([[0.8, 2.2, 3.6], [2.0, 3.0, 4.0], [1.2, 2.0, 5.8]])

result = sp.linalg.lu(A)

print("P =\n", result[0])
print("L =\n", result[1])
print("R =\n", result[2])
