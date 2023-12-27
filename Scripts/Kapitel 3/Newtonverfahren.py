from sympy import diff, exp, symbols


def newtonverfahren_anzahl_iterationen(funktion, x_0, iterations):
    abgeleitete_funktion = diff(funktion)
    for i in range(iterations):
        print(funktion.subs(x, x_0).evalf())
        print(abgeleitete_funktion.subs(x, x_0).evalf())
        x_n = x_0 - (
            funktion.subs(x, x_0).evalf() / abgeleitete_funktion.subs(x, x_0).evalf()
        )
        print(f"x_{i} = {x_0} -> {x_n}")
        x_0 = x_n
    return x_n


x = symbols("x")
funktion = exp(x**2) + x**-3 - 10
x_0 = 2
iterationen = 5
newtonverfahren_anzahl_iterationen(funktion, x_0, iterationen)

# Beispiele aus Zusatzübung
# x = symbols("x")
# funktion = x - 0.4 * sin(x) - 0.4
# x_0 = 0.7
# iterationen = 1
# newtonverfahren_anzahl_iterationen(funktion, x_0, iterationen)
