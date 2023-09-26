import numpy as np
import matplotlib.pyplot as plt



def polynom (vector, min, max):
    i = 0
    x = np.arange(min, max, 0.1)
    f = 0
    print(len(vector))
    while i < len(vector):
        f += vector[i] * x ** (len(vector) - i - 1)
        i += 1
        print(i)

    i = 0
    p = np.arange(len(vector) - 1)
    while i < len(vector) - 1:
        p[i] = vector[i] * (len(vector) - i - 1)
        i += 1
    print(p)
    return f

polynom([3, 2, 1], -5, 5)