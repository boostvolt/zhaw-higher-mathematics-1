import numpy as np


def spektral_radius(matrix, debug=False):
    eigenwerte = np.linalg.eigvals(matrix)
    eigenwerte_betrag = np.abs(eigenwerte)

    if debug:
        print(f"Eigenwerte: {eigenwerte}")
        print(f"Eigenwerte im Betrag: {eigenwerte_betrag}")
        print()

    return np.max(eigenwerte_betrag)


########################################################################################

# Matrix definieren
matrix = np.array([[1, 0, 0], [2, 3, 0], [0, 1, 2]])

print(f"Spektralradius: {spektral_radius(matrix, True)}")
