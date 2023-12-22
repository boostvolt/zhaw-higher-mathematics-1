from sympy import symbols, diff, pi, exp, log, cos, sin


def konditionszahl(funktion, variable, punkt):
    ableitung_funktion = diff(funktion, variable)

    f_wert = funktion.subs(variable, punkt)
    f_ableitung_wert = ableitung_funktion.subs(variable, punkt)

    if f_ableitung_wert != 0:
        konditionszahl_wert = (abs(f_ableitung_wert) * abs(punkt)) / abs(f_wert)
        return konditionszahl_wert
    else:
        return "Konditionszahl kann nicht berechnet werden (Ableitung an diesem Punkt ist Null)."


# Beispielaufruf

variable = symbols("x")  # Unbekannte hier definieren (x, y, z etc.)
funktion = sin(
    variable
)  # Die Funktion hier angeben, beachte mit sympy Sachen wie cos, sin, exp zu benutzen! Einige sind schon oben importiert
# funktion = exp(variable)
punkt = 2  # Der Punkt (x), an dem du die Konditionszahl berechnen möchtest


resultat = konditionszahl(funktion, variable, punkt)
print(f"Die Konditionszahl der Funktion {funktion} an x = {punkt} ist: {resultat}")
