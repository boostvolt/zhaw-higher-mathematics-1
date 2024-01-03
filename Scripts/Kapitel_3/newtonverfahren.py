from sympy import diff, sympify


def newtonverfahren_anzahl_iterationen(funktion, x_0, iterationen, debug=False):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    abgeleitete_funktion = diff(funktion)

    for i in range(iterationen):
        x_n = x_0[str(symbols[0])] - (
            funktion.subs(x_0).evalf() / abgeleitete_funktion.subs(x_0).evalf()
        )

        if debug:
            print(f"---- Iteration {i + 1}")
            print(f"f({symbols[0]}_{i}) = {funktion.subs(x_0).evalf()}")
            print(f"f'({symbols[0]}_{i}) = {abgeleitete_funktion.subs(x_0).evalf()}")
            print(f"{symbols[0]}_{i + 1} = {x_n}")
            print()

        x_0[str(symbols[0])] = x_n

    return x_0[str(symbols[0])]


########################################################################################

# Funktion definieren
funktion = "exp(x**2) + x**-3 - 10"

# Wert für x_0 definieren
x_0 = {"x": 2}

# Anzahl der Iterationen
iterationen = 5

print(
    f"{list(x_0.keys())[0]}_{iterationen} = {newtonverfahren_anzahl_iterationen(funktion, x_0, iterationen, True)}"
)

# Beispiele aus Zusatzübung
# funktion = "x - 0.4 * sin(x) - 0.4"
# werte = {"x": 0.7}
# iterationen = 1
