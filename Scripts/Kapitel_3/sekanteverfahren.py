from sympy import sympify


def sekanteverfahren_toleranz(funktion, x_0, x_1, toleranz, debug=False):
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    i = 0
    while abs(x_1[str(symbols[0])] - x_0[str(symbols[0])]) > toleranz:
        x_1[str(symbols[0])], x_0[str(symbols[0])] = (
            x_1[str(symbols[0])]
            - (
                (x_1[str(symbols[0])] - x_0[str(symbols[0])])
                / (funktion.subs(x_1) - funktion.subs(x_0))
            )
            * funktion.subs(x_1),
            x_1[str(symbols[0])],
        )

        if debug:
            print(f"---- Iteration {i + 1}")
            print(f"f({symbols[0]}_{i}) = {funktion.subs(x_0).evalf()}")
            print(f"f({symbols[0]}_{i+1}) = {funktion.subs(x_1).evalf()}")
            print(f"{symbols[0]}_{i + 2} = {x_1}")
            print()

        i += 1

    return x_1[str(symbols[0])]


def sekanteverfahren_anzahl_iterationen(funktion, x_0, x_1, iterationen, debug=False):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    for i in range(iterationen):
        x_1[str(symbols[0])], x_0[str(symbols[0])] = (
            x_1[str(symbols[0])]
            - (
                (x_1[str(symbols[0])] - x_0[str(symbols[0])])
                / (funktion.subs(x_1) - funktion.subs(x_0))
            )
            * funktion.subs(x_1),
            x_1[str(symbols[0])],
        )

        if debug:
            print(f"---- Iteration {i + 1}")
            print(f"f({symbols[0]}_{i}) = {funktion.subs(x_0).evalf()}")
            print(f"f({symbols[0]}_{i+1}) = {funktion.subs(x_1).evalf()}")
            print(f"{symbols[0]}_{i + 2} = {x_1}")
            print()

    return x_1[str(symbols[0])]


########################################################################################

# Beispiel mit 2 Funktionen die einen Schnittpunkt haben

# Funktion definieren
funktion_1 = sympify("(x**2 + 1) ** 2 - 10")
funktion_2 = sympify("5 / ((x - 1) ** 2 + 1)")
funktion = funktion_1 - funktion_2

# Wert für x_0 definieren
x_0 = {"x": 1.6}

# Wert für x_1 definieren
x_1 = {"x": 1.7}

# Fixpunkt mit Toleranz berechnen
# Toleranz definieren
toleranz = 10**-6

sekanteverfahren_toleranz(funktion, x_0, x_1, toleranz, True)

# Sekantenverfahren mit angegebener Anzahl Iterationen berechnen
# Anzahl der Iterationen
# iterationen = 2

# sekanteverfahren_anzahl_iterationen(funktion, x_0, x_1, iterationen, True)
