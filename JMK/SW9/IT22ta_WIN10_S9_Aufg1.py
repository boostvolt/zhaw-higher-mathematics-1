import numpy.linalg as l
import numpy as np

A = np.array([[1, 0, 2], [0, 1, 0], [10 ** (-4), 0, 10 ** (-4)]])
bTilde = np.array([1, 1, 1.66658 * 10 ** (-7)])

xTilde = l.solve(A, bTilde)

x = np.array([-1, 1, 1])

print(l.norm(x - xTilde, np.inf) / l.norm(x, np.inf))

e = 6.56583 * 10 ** (-8)
print((60003 / (1 - (60003 * 10 ** (-7)))) * (((3 * 10 ** (-7)) / 3) + (e / 1)))

A = np.array([])
