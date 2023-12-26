import numpy as np

A = np.array([[5, -2], [0, -6]])

# 1-Norm, Spaltensummennorm
print("1-Norm, Spaltensummennorm: {}".format(np.linalg.norm(A, 1)))

# 2-Norm, Spektralnorm
print("2-Norm, Spektralnorm: {}".format(np.linalg.norm(A, 2)))

# ∞-Norm, Zeilensummennorm
print("∞-Norm, Zeilensummennorm: {}".format(np.linalg.norm(A, np.inf)))
