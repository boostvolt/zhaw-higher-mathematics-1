import numpy.linalg as lin
import numpy as np

A = np.array([[1, 0, 2], [0, 1, 0], [10 ** (-4), 0, 10 ** (-4)]])
bTilde = np.array([1, 1, 1.66658 * 10 ** (-7)])

x = np.array([-1, 1, 1])
xTilde = lin.solve(A, bTilde)

print(lin.norm(x - xTilde, np.inf) / lin.norm(x, np.inf))

condA = 60003
relA = 10 ** (-7)
epsilon = 6.56583
normA = 3
disNormA = 3 * 10 ** (-7)
exponent = 1
while (60003 / (1 - (condA * relA))) * (((disNormA) / 3) + ((epsilon * 10 ** (-exponent)) / 1)) > 0.01:
    exponent += 1

print(exponent)
#Der relative Fehler beträgt 6.56583 * 10^(-8)