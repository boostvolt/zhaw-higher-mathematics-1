import numpy as np
import timeit

# Factorial of 6 is 720


def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise ValueError("Error: The factorial is defined only for positive integers")

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


# This for-loop function is faster than the recursive function by a factor of 5,2.
#
# Explanation:
# For recursive functions, there is an overhead for each function call.
# Each call to fact_rec creates a new function frame on the stack that requires memory.
# This overhead is not present in the for loop because it calls only one function.
def fact_for(n):
    if n < 0 or np.trunc(n) != n:
        raise ValueError("Error: The factorial is defined only for positive integers")

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

# In Python 3, integer is dynamically increased if the size of the result requires.
# This means that you can theoretically compute very large factorials as long as your memory and hardware allow.

for n in range(190, 201):
    print("fact_rec({}) = {}".format(n, fact_rec(n)))
    print("fact_for({}) = {}".format(n, fact_for(n)))

# On the other hand float has a maximum size according to the IEEE-754 because it is a floating point number.
# Factorial does not work with floating point number. It must be a positive integer.
# Therefore we get an OverflowError: int too large to convert to float

for n in range(170, 172):
    print("fact_rec({}) = {}".format(n, float(fact_rec(n))))
    print("fact_for({}) = {}".format(n, float(fact_for(n))))
