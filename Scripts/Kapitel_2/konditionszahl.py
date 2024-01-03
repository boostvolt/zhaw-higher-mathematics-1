import numpy as np
from sympy import diff, sympify


def konditionszahl_bewertung(konditionszahl):
    if konditionszahl <= 10:
        return "Gut konditioniert"

    return "Schlecht konditioniert"


def konditionszahl(funktion, werte):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    abgeleitete_funktion = diff(funktion)

    funktion_wert = funktion.subs(werte).evalf()
    abgeleitete_funktion_wert = abgeleitete_funktion.subs(werte).evalf()

    if abgeleitete_funktion_wert == 0:
        raise ValueError(
            "Konditionszahl kann nicht berechnet werden (Ableitung an diesem Punkt ist Null)."
        )

    return (np.abs(abgeleitete_funktion_wert) * abs(werte[str(symbols[0])])) / abs(
        funktion_wert
    )


########################################################################################

# Funktion definieren
funktion = "1 - exp(x)"

# Werte für Unbekannte definieren
werte = {"x": 1}

print(f"Konditionszahl: {konditionszahl(funktion, werte).evalf()}")
print(f"Bewertung: {konditionszahl_bewertung(konditionszahl(funktion, werte))}")
