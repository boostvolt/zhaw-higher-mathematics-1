import numpy as np

A = np.array([[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]])
B = np.array([[5, 4, 3, 2], [4, 3, 2, 5], [3, 2, 5, 4], [2, 5, 4, 3]])
c = np.array([1, 2, 3, 4])

# Aufgabe 1 a)
print("Aufgabe 1 a)")
print(A.dot(c))
print(B.dot(c))
print(A.T)
print(B.T)
print((A.T).dot(A))
print((B.T).dot(B))

# Aufgabe 1 b)
print("Aufgabe 1 b)")
print(A[[3], :] * (B[:, [1]]))

# Aufgabe 1 c)
print("Aufgabe 1 c)")
print(np.sum(A, axis=0))
print(np.sum(B, axis=1))
