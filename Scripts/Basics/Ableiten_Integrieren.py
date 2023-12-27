from sympy import diff, sqrt, symbols


def ableitung(funktion):
    return diff(funktion, x)


x = symbols("x")  # Unbekannten hier definieren

# Beispielaufrufe
# funktion = exp(x)  # Für e^x
# funktion = sin(x)
# funktion = cos(x)
# funktion = log(x)
# funktion = log(x, 2) # Mit Basis 2
# funktion = (x**3 + 4) ** -2  # Für (x^3 + 4)^(-2)
# funktion = 1 - exp(x)
# funktion = 1 + (1 / x) + (1 / x**2)
# funktion = 1 - x**2
funktion = sqrt(1 - x)

resultat = ableitung(funktion)
print(f"Die Ableitung von {funktion} ist: {resultat}")

# Hier X einsetzen und das Ergebnis für die abgeleitete Funktion erhalten
print(resultat.subs(x, 0.5))
