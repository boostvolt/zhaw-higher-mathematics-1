from sympy import diff, sympify


def ableiten(funktion, symbol=None):
    funktion = sympify(funktion)

    if symbol is None:
        return diff(funktion)

    return diff(funktion, symbol)


########################################################################################

# Funktion definieren
funktion = "sqrt(1 - x)"
# funktion = "exp(x)" # Für e^x
# funktion = "sin(x)"
# funktion = "cos(x)"
# funktion = "log(x)"
# funktion = "log(x, 2)" # Mit Basis 2
# funktion = "(x**3 + 4) ** -2" # Für (x^3 + 4)^(-2)
# funktion = "1 - exp(x)"
# funktion = "1 + (1 / x) + (1 / x**2)"
# funktion = "1 - x**2"

print(f"Ableitung: {ableiten(funktion)}")
# print(f"Ableitung: {ableiten(funktion, 'x')}") # Für Ableitung nach x (bei mehreren freien Variablen

# Werte für Unbekannte definieren
# werte = {"x": 0.8}

# print(f"Ergebniss von Ableitung: {ableiten(funktion).subs(werte).evalf()}")
# print(f"Ergebniss von Funktion: {sympify(funktion).subs(werte).evalf()}")
