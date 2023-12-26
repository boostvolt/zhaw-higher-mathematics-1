import numpy as np

V = np.array([[1], [-2]])

# 1-Norm, Spaltennorm
print("1-Norm, Spaltennorm: {}".format(np.linalg.norm(V, 1)))

# 2-Norm, euklidische Norm
print("2-Norm, euklidische Norm: {}".format(np.linalg.norm(V, 2)))

# ∞-Norm, Maximumnorm
print("∞-Norm, Maximumnorm: {}".format(np.linalg.norm(V, np.inf)))
