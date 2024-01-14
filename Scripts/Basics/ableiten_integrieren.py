from sympy import diff, sympify


def ableiten(funktion, symbol=None):
    funktion = sympify(funktion)

    if symbol is None:
        return diff(funktion)

    return diff(funktion, symbol)


########################################################################################

# Funktion definieren
funktion = "sqrt(1 - x)"

print(f"Ableitung: {ableiten(funktion)}")
# print(f"Ableitung: {ableiten(funktion, 'x')}") # Für Ableitung nach x (bei mehreren freien Variablen

# Werte für Unbekannte definieren
# werte = {"x": 0.8}

# print(f"Ergebniss von Ableitung: {ableiten(funktion).subs(werte).evalf()}")
# print(f"Ergebniss von Funktion: {sympify(funktion).subs(werte).evalf()}")
