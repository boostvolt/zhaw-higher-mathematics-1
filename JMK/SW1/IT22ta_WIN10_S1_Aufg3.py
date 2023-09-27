import numpy as np
import timeit


def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise ValueError("Error: The facotiral is defined only for positive integers")

    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)


print(
    "Average execution time of fact_rec: {} seconds".format(
        np.mean(
            timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
        )
    )
)


# This for-loop function is faster than the recursive function by a factor of 6.846.
def fact_for(n):
    if n < 0 or np.trunc(n) != n:
        raise ValueError("Error: The facotiral is defined only for positive integers")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


print(
    "Average execution time of fact_for: {} seconds".format(
        np.mean(
            timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)
        )
    )
)
