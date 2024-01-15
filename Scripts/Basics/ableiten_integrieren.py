from sympy import diff, integrate, sympify


def ableiten(funktion, symbol=None):
    funktion = sympify(funktion)

    if symbol is None:
        return diff(funktion)

    return diff(funktion, symbol)


def integrieren(funktion, symbol=None):
    funktion = sympify(funktion)

    if symbol is None:
        return integrate(funktion)

    return integrate(funktion, symbol)


########################################################################################

# Funktion definieren
funktion = "sqrt(1 - x)"

print(f"Ableitung: {ableiten(funktion)}")
# print(f"Ableitung: {ableiten(funktion, 'x')}") # Für Ableitung nach x (bei mehreren freien Variablen
# print(f"Integral: {integrieren(funktion)}")

# Werte für Unbekannte definieren
# werte = {"x": 0.8}

# print(f"Ergebniss von Ableitung: {ableiten(funktion).subs(werte).evalf()}")
# print(f"Ergebniss von Funktion: {sympify(funktion).subs(werte).evalf()}")
