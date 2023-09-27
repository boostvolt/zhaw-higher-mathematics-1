import numpy as np
import matplotlib.pyplot as plt

vector = np.array([3, 2, 5, 3, 1])
deriv_vector = np.array([])
i = len(vector)
position = 0
while i > 0:
    exponent = i - 1
    vector[position] = vector[position] * exponent

    i = i - 1
    position = position + 1

print(deriv_vector)
