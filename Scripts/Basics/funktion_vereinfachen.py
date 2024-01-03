from sympy import simplify


def funktion_vereinfachen(funktion):
    return simplify(funktion)


########################################################################################

# Funktion definieren
funktion = "x - ((x**2 -c) / 2*x)"

print(f"Vereinfachte Funktion: {funktion_vereinfachen(funktion)}")
