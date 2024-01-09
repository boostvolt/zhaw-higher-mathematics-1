import numpy as np


def vektor_norm(vektor, norm):
    norm_symbol = norm
    if norm == np.inf:
        norm_symbol = "∞"

    # TODO: Add debug output

    return norm_symbol, np.linalg.norm(vektor, norm)


########################################################################################

# Vektor definieren
vektor = np.array([[1], [-2]])

# Norm definieren (1, 2, np.inf)
norm = np.inf

[norm_symbol, norm] = vektor_norm(vektor, norm)
print(f"Vektor {norm_symbol}-Norm: {norm}")
