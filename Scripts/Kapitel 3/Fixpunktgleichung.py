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


def start_fixpunktiteration_anzahl_iterationen(startwert, anzahl_iterationen):
    previous_value = startwert
    next_x_value = -100

    for i in range(anzahl_iterationen):
        # Nur für die erste Iteration nicht machen
        if i > 0:
            previous_value = next_x_value
        next_x_value = fixpunktiteration(previous_value)
        print(f"x_{i} = {previous_value} -> {next_x_value}")


# Hier Variable für Funktion definieren
x = symbols("x")
# Hier Funktion definieren, welche schon nach x aufgelöst sein muss!
funktion = (230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221
startwert = 0
toleranz = 10**-6
start_fixpunktiteration_toleranz(startwert, toleranz)
start_fixpunktiteration_anzahl_iterationen(startwert, 5)

# x = symbols("x")
# Funktion muss schon nach x aufgelöst sein!
# funktion = exp(x) - exp(1)
# startwert = -2.5
# toleranz = 10**-5
# start_fixpunktiteration(startwert, toleranz)
