import numpy as np
import scipy as sp

A = np.array([[0.8, 2.2, 3.6], [2.0, 3.0, 4.0], [1.2, 2.0, 5.8]])

print(sp.linalg.lu(A))

