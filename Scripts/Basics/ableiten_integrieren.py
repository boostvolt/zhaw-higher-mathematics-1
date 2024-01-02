from sympy import diff, sympify


def ableiten(funktion):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    return diff(funktion, symbols[0])


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

# Werte für Unbekannte definieren
werte = {"x": 0.8}

print(f"Ergebniss von Ableitung: {ableiten(funktion).subs(werte)}")
print(f"Ergebniss von Funktion: {sympify(funktion).subs(werte)}")
