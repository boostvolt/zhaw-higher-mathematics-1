import numpy as np
import numpy.linalg as l

A = np.array([[1, 0, 2], [0, 1, 0], [10 ** (-4), 0, 10 ** (-4)]])
bTilde = np.array([1, 1, 1.66658 * 10 ** (-7)])

x = np.array([-1, 1, 1])
xTilde = l.solve(A, bTilde)

print(l.norm(x - xTilde, np.inf) / l.norm(x, np.inf))


exponent = 1
while (60003 / (1 - (60003 * 10 ** (-7)))) * (
    ((3 * 10 ** (-7)) / 3) + ((6.56583 * 10 ** (-exponent)) / 1)
) > 0.01:
    exponent += 1

print(exponent)
# e (epsilon) must not exceed 6.56583 * 10^(-8)
