import numpy as np
import matplotlib.pyplot as plt

# Beispiel: p(x) = x^2 + x + 1 in [0,1]
# Für x erwarten wir alle Werte zwischen 0 und 1 im Abstand von 0.1
# Für p(x) erwarten wir array([1., 1.11, 1.24, 1.39, 1.56, 1.75, 1.96, 2.19, 2.44, 2.71])
# Für dp(x) erwarten wir array([1., 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8])
# Für pint(x) erwarten wir array([0., 0.10533333, 0.22266667, 0.354, 0.50133333,0.66666667, 0.852, 1.05933333, 1.29066667, 1.548])


def polynom (vector, min, max):
    if len(vector.shape) != 1 or vector.size == 0:
        raise ValueError("Error: a must be a non-empty row or column vector")

    i = 0
    x = np.arange(min, max, 0.1)

    p = 0
    while i < len(vector):
        p += vector[i] * x ** (len(vector) - i - 1)
        i += 1

    i = 0
    vector_p = np.arange(len(vector) - 1, dtype="float64")
    while i < len(vector) - 1:
        vector_p[i] =  vector[i] * (len(vector) - i - 1)
        i += 1

    dp = 0
    i = 0
    while i < len(vector_p):
        dp += vector_p[i] * x ** (len(vector_p) - i - 1)
        i += 1

    vector_p_int = np.arange(len(vector) + 1,  dtype="float64")
    i = 0
    while i < len(vector):
        vector_p_int[i] = vector[i] / (len(vector) - i)
        i += 1
    vector_p_int[len(vector_p_int) -1] = 0

    pint = 0
    i = 0
    while i < len(vector_p_int):
        pint += vector_p_int[i] * x ** (len(vector_p_int) - i - 1)
        i += 1

    return(x,p,dp,pint)

print(polynom(np.array([1,1,1]), 0, 1))