from collections import Counter

import numpy as np


def algebraische_vielfachheit(matrix):
    eigenwerte = np.linalg.eigvals(matrix)
    eigenwerte = np.round(eigenwerte, 10)
    eigenwerte = [
        val.real if np.isclose(val.imag, 0, atol=1e-10) else val for val in eigenwerte
    ]

    return dict(Counter(eigenwerte))


########################################################################################

# Matrix definieren
A = np.array([[1, 1, 1], [0, 2, 0], [1, -1, 1]])

print(f"Algebraische Vielfachheit: {algebraische_vielfachheit(A)}")
