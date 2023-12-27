from sympy import diff, exp, symbols


def abstossender_anziehender_fixpunkt_mit_gegebenem_fixpunkt(funktion, x, fixpunkt):
    # Ableitung einer Funktion
    abgeleitete_funktion = diff(funktion, x)
    result = abgeleitete_funktion.subs(x, fixpunkt)
    print(
        "Die abgeleitete Funktion ist {} und ergibt {} mit dem Fixpunkt {}".format(
            abgeleitete_funktion, result.evalf(), fixpunkt
        )
    )
    if abs(result) < 1:
        print(
            f"Es handelt sich hier um einen anziehenden Fixpunkt, weil |F'(x̄)| = {abs(result.evalf())} < 1"
        )
    else:
        print(
            f"Es handelt sich hier um einen abstossenden Fixpunkt, weil |F'(x̄)| = {abs(result.evalf())} > 1"
        )


def abstossender_anziehender_fixpunkt_mit_intervall(funktion, x, startwert, endwert):
    # Ableitung einer Funktion
    abgeleitete_funktion = diff(funktion, x)
    result_ableitung_startwert = abgeleitete_funktion.subs(x, startwert)
    result_ableitung_endwert = abgeleitete_funktion.subs(x, endwert)

    if result_ableitung_startwert < 1 and result_ableitung_endwert.evalf() < 1:
        print("Anziehender Fixpunkt im Intervall [{}, {}]".format(startwert, endwert))
        print(
            "Beweis: f'({}) = {} <= f'(x̄) <= f'({}) = {} < 1".format(
                startwert, result_ableitung_startwert, endwert, result_ableitung_endwert
            )
        )
    elif 1 < result_ableitung_startwert and 1 < result_ableitung_endwert:
        print("Abstossender Fixpunkt im Intervall [{}, {}]".format(startwert, endwert))
        print(
            "Beweis: 1 < f'({}) = {} <= f'(x̄) <= f'({}) = {}".format(
                startwert, result_ableitung_startwert, endwert, result_ableitung_endwert
            )
        )


# # Variable definieren
x = symbols("x")

# # Funktion definieren
# # Funktion muss schon nach x auflöst sein!
funktion = (230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221

# Bekannter Fixpunkt
fixpunkt = 0

# # Herausfinden ob Fixpunkt anziehend oder abstossend mit gegebenem Fixpunkt
abstossender_anziehender_fixpunkt_mit_gegebenem_fixpunkt(funktion, x, fixpunkt)

funktion = exp(x) - exp(1)
startwert = -3
endwert = -2

# Anziehender Fixpunkt
abstossender_anziehender_fixpunkt_mit_intervall(funktion, x, -3, -2)


# Beipiele aus den Aufgaben
# funktion = exp(x) - exp(1)

# Abstossender Fixpunkt
# fixpunkt = 2
# abstossender_anziehender_fixpunkt_mit_gegebenem_fixpunkt(funktion, x, fixpunkt)

# Abstossender Fixpunkt
# startwert = -3
# endwert = -2
# abstossender_anziehender_fixpunkt_mit_intervall(funktion, x, 1, 2)
