from sympy import symbols, diff, cos, sin, pi, log


def ableitung(funktion):
    ableitung = diff(funktion, x)
    return ableitung


x = symbols("x")  # Unbekannten hier definieren

# Beispielaufrufe
# funktion = exp(x)  # Für e^x
# funktion = sin(x)
# funktion = cos(x)
# funktion = log(x)
# funktion = log(x, 2) # Mit Basis 2
funktion = (x**3 + 4) ** -2  # Für (x^3 + 4)^(-2)

resultat = ableitung(funktion)
print(f"Die Ableitung von {funktion} ist: {resultat}")
