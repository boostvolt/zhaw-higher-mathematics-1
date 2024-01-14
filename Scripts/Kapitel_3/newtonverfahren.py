from sympy import diff, sympify


def newtonverfahren_toleranz(funktion, x_0, toleranz, debug=False):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    abgeleitete_funktion = diff(funktion)

    x_n = x_0[str(symbols[0])]
    i = 0
    while True:
        x_n_minus_1 = x_n
        x_n = x_n_minus_1 - (
            funktion.subs({str(symbols[0]): x_n_minus_1}).evalf()
            / abgeleitete_funktion.subs({str(symbols[0]): x_n_minus_1}).evalf()
        )

        if debug:
            print(f"---- Iteration {i + 1}")
            print(
                f"f({symbols[0]}_{i}) = {funktion.subs({str(symbols[0]): x_n_minus_1}).evalf()}"
            )
            print(
                f"f'({symbols[0]}_{i}) = {abgeleitete_funktion.subs({str(symbols[0]): x_n_minus_1}).evalf()}"
            )
            print(f"{symbols[0]}_{i + 1} = {x_n}")
            print()

        if abs(x_n - x_n_minus_1) < toleranz:
            break

        i += 1

    return x_n


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
funktion = "exp(x) - (sqrt(x) + 2)"

# Wert für x_0 definieren
x_0 = {"x": 0.5}

# Newtonverfahren mit Toleranz berechnen
# Toleranz definieren
toleranz = 10**-7

newtonverfahren_toleranz(funktion, x_0, toleranz, True)

# Newtonverfahren mit angegebener Anzahl Iterationen berechnen
# Anzahl der Iterationen
# iterationen = 5

# newtonverfahren_anzahl_iterationen(funktion, x_0, iterationen, True)
