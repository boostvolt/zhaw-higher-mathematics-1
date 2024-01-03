import numpy as np
from sympy import sympify


def fixpunktiteration(funktion, wert):
    return funktion.subs(wert).evalf()


def start_fixpunktiteration_toleranz(funktion, x_0, toleranz):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    previous_value = x_0[str(symbols[0])]
    next_x_value = -100
    iteration_count = 0

    while np.abs(next_x_value - previous_value) > toleranz:
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            previous_value = next_x_value

        next_x_value = fixpunktiteration(funktion, {symbols[0]: previous_value})
        iteration_count = iteration_count + 1

        print(f"{symbols[0]}_{iteration_count} = {next_x_value}")

    print()
    return next_x_value


def start_fixpunktiteration_anzahl_iterationen(funktion, x_0, iterationen):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    previous_value = x_0[str(symbols[0])]
    next_x_value = -100

    for i in range(iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value

        next_x_value = fixpunktiteration(funktion, {symbols[0]: previous_value})

        print(f"{symbols[0]}_{i + 1} = {next_x_value}")

    print()
    return next_x_value


########################################################################################

# Funktion definieren (muss schon nach x augelöst sein)
funktion = "(230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221"

# Wert für x_0 definieren
x_0 = {"x": 0}

# Fixpunkt mit Toleranz berechnen
# Toleranz definieren
toleranz = 10**-6

print(f"Fixpunkt: {start_fixpunktiteration_toleranz(funktion, x_0, toleranz)}")

# Fixpunkt mit angegebener Anzahl Iterationen berechnen
# Anzahl der Iterationen
iterationen = 10

print()
print(
    f"Fixpunkt: {start_fixpunktiteration_anzahl_iterationen(funktion, x_0, iterationen)}"
)

# Beispiel 1
# funktion = "exp(-x)"
# x_0 = {"x": 0.8}
# iterationen = 3
# start_fixpunktiteration_anzahl_iterationen(funktion, x_0, iterationen)

# Beispiel 2
# funktion = "1 + (1 / x) + (1 / x**2)"
# x_0 = {"x": 1.8}
# iterationen = 2
# start_fixpunktiteration_anzahl_iterationen(funktion, x_0, iterationen)

# Beispiel 3
# funktion = "sqrt(1 - x)"
# x_0 = {"x": 0.5}
# iterationen = 2
# start_fixpunktiteration_anzahl_iterationen(funktion, x_0, iterationen)
