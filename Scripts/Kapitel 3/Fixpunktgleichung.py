import numpy as np
from sympy import diff, exp, symbols, log


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

def abstossender_anziehender_fixpunkt_mit_x0(funktion, x, value):
    #Ableitung einer Funktion
    abgeleitete_funktion = diff(funktion, x)
    result = abgeleitete_funktion.subs(x, value)
    print ("Die abgeleitete Funktion ist {} und ergibt {} mit dem Startwert {}".format(abgeleitete_funktion, result.evalf(), value))
    if (abs(result) < 1):
        print ("Es handelt sich hier um einen anziehenden Fixpunkt")
    else:
        print ("Es handelt sich hier um einen abstossenden Fixpunkt")

def abstossender_anziehender_fixpunkt_mit_fixpunkt(funktion, x, startwert, endwert, fixpunkt):
    #Ableitung einer Funktion
    abgeleitete_funktion = diff(funktion, x)
    result_ableitung_fixpunkt = abgeleitete_funktion.subs(x, fixpunkt)
    result_ableitung_startwert = abgeleitete_funktion.subs(x, startwert)
    result_ableitung_endwert = abgeleitete_funktion.subs(x, endwert)
    if (0 < result_ableitung_fixpunkt.evalf() and result_ableitung_fixpunkt.evalf() <= result_ableitung_endwert.evalf() and result_ableitung_endwert.evalf() < 1):
        print("Anziehender Fixpunkt mit Startwert {}".format(startwert))
        print("Beweis: 0 < f'(x̄) <= f'({}) = {} < 1".format(startwert, result_ableitung_startwert))
    elif (1 < result_ableitung_startwert and result_ableitung_startwert <= result_ableitung_fixpunkt and result_ableitung_fixpunkt <= result_ableitung_endwert):
        print("Abstossender Fixpunkt mit Startwert {} und Endwert {}".format(startwert, endwert))
        print("Beweis: 1 < f'({}) <= f'(x̄) <= f'({})".format(startwert, result_ableitung_startwert, endwert))

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
# Herausfinden ob Fixpunkt anziehend oder abstossend mit x0 Wert
abstossender_anziehender_fixpunkt_mit_x0(funktion, x, startwert)
# Herausfinden ob Fixpunkt anziehend oder abstossend mit Fixpunkt
abstossender_anziehender_fixpunkt_mit_fixpunkt(funktion, x, startwert, endwert, fixpunkt)
# Berechne Fixpunkt mit angegebener Anzahl Iterationen
start_fixpunktiteration_anzahl_iterationen(startwert, 10)


#Beispiel 1
funktion = exp(x) - exp(1)
startwert = -3
toleranz = 10**-5
# Anziehender Fixpunkt
fixpunkt = start_fixpunktiteration_toleranz(startwert, toleranz)
abstossender_anziehender_fixpunkt_mit_x0(funktion, x, startwert)
abstossender_anziehender_fixpunkt_mit_fixpunkt(funktion, x, -3, -2, fixpunkt)
# Abstossender Fixpunkt
abstossender_anziehender_fixpunkt_mit_x0(funktion, x, 2)
abstossender_anziehender_fixpunkt_mit_fixpunkt(funktion, x, 1, 2, 2)