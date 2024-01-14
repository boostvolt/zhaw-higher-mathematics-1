import numpy as np

# Example with following input: p(x) = 2x^2 + x + 2 for intervall [0,1] with steps 0.1
# Expected outputs:
# p(x) = array([2., 2.12, 2.28, 2.48, 2.72, 3., 3.32, 3.68, 4.08, 4.52, 5.])
# dp(x) = array([1., 1.4, 1.8, 2.2, 2.6, 3., 3.4, 3.8, 4.2, 4.6, 5.])
# pint(x) = array([0., 0.20566667, 0.42533333, 0.663, 0.92266667, 1.20833333, 1.524, 1.87366667, 2.26133333, 2.691, 3.16666667])


def task_two(a, xmin, xmax):
    if len(a.shape) != 1 or a.size == 0:
        raise ValueError("Error: a must be a non-empty row or column vector")

    n = len(a) - 1
    x = np.arange(xmin, xmax + 0.1, 0.1)

    p = np.zeros_like(x)
    for i in range(n + 1):
        p += a[i] * x ** (n - i)

    dp = np.zeros_like(x)
    for i in range(n):
        dp += (n - i) * a[i] * x ** (n - i - 1)

    pint = np.zeros_like(x)
    for i in range(n + 1):
        pint += (a[i] / (n - i + 1)) * x ** (n - i + 1)

    return (x, p, dp, pint)


print(task_two(np.array([2, 1, 2]), 0, 1))
