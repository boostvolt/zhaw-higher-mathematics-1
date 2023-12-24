from sympy import symbols, diff, pi, exp, log, cos, sin
import numpy as np


def konditionszahl(funktion, x, punkt):
    ableitung_funktion = diff(funktion, x)

    f_wert = funktion.subs(x, punkt).evalf()
    f_ableitung_wert = ableitung_funktion.subs(x, punkt).evalf()

    if f_ableitung_wert != 0:
        konditionszahl_wert = (np.abs(f_ableitung_wert) * abs(punkt)) / abs(f_wert)
        return konditionszahl_wert
    else:
        return "Konditionszahl kann nicht berechnet werden (Ableitung an diesem Punkt ist Null)."


# Beispielaufrufe

x = symbols("x")
# funktion = sin(x)  # Die Funktion hier angeben, beachte mit sympy Sachen wie cos, sin, exp zu benutzen! Einige sind schon oben importiert
# funktion = exp(x)

funktion = 1 - exp(x)
punkt = 1  # Der Punkt (x), an dem du die Konditionszahl berechnen möchtest
resultat = konditionszahl(funktion, x, punkt)
print(
    f"Die Konditionszahl der Funktion {funktion} an x = {punkt} ist: {resultat.evalf()}"
)
