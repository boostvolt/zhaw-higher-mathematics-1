import numpy as np

def task_two(a, xmin, xmax):
    if len(a.shape) != 1 or a.size == 0:
        raise ValueError("Error: a must be a non-empty row or column vector")

    n = len(a) - 1
    x = np.arange(xmin, xmax + 0.1, 0.1)

    p = np.zeros_like(x)
    for i in range(n + 1):
        p += a[i] * x ** (n - i)

    dp = np.zeros_like(x)
    for i in range(n + 1):
        dp += (n - i) * a[i] * x ** (n - i - 1)

    pint = np.zeros_like(x)
    for i in range(n + 1):
        pint += (a[i] / (n - i + 1)) * x ** (n - i + 1)

    return (x, p, dp, pint)

print(task_two(np.array([2, 4, 6]), -3, 3))
