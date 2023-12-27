import numpy as np
from sympy import symbols


def fixpunktiteration(value):
    return funktion.subs(x, value).evalf()


def start_fixpunktiteration_toleranz(startwert, toleranz):
    previous_value = startwert
    next_x_value = -100
    iteration_count = 0

    while np.abs(next_x_value - previous_value) > toleranz:
        # Nur für die erste Iteration nicht machen
        if iteration_count > 0:
            previous_value = next_x_value
        next_x_value = fixpunktiteration(previous_value)
        print(f"x_{iteration_count} = {previous_value} -> {next_x_value}")
        iteration_count = iteration_count + 1
    # Gebe Fixpunkt zurück
    return next_x_value


def start_fixpunktiteration_anzahl_iterationen(startwert, anzahl_iterationen):
    previous_value = startwert
    next_x_value = -100

    for i in range(anzahl_iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value
        next_x_value = fixpunktiteration(previous_value)
        print(f"x_{i} = {previous_value} -> {next_x_value}")


# Variable definieren
x = symbols("x")

# Funktion definieren
# Funktion muss schon nach x auflöst sein!
funktion = (230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221

# Startwert & Endwert definieren
startwert = 0
endwert = 1

# Toleranz definieren
toleranz = 10**-6

# Fixpunkt mit Toleranz berechnen
fixpunkt = start_fixpunktiteration_toleranz(startwert, toleranz)
print("Fixpunkt: ", fixpunkt)

# Berechne Fixpunkt mit angegebener Anzahl Iterationen
start_fixpunktiteration_anzahl_iterationen(startwert, 10)

# # Beispiel 1
# x = symbols("x")
# funktion = exp(-x)
# start_fixpunktiteration_anzahl_iterationen(0.8, 3)

# # Beispiel 2
# x = symbols("x")
# funktion = 1 + (1 / x) + (1 / x**2)
# start_fixpunktiteration_anzahl_iterationen(1.8, 2)

# # Beispiel 3
# x = symbols("x")
# funktion = sqrt(1 - x)
# start_fixpunktiteration_anzahl_iterationen(0.5, 2)
