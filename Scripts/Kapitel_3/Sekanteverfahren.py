from sympy import symbols


def sekanteverfahren_anzahl_iterationen(funktion, x0, x1, anzahl_iterationen):
    for i in range(anzahl_iterationen):
        x1, x0 = (
            x1
            - ((x1 - x0) / (funktion.subs(x, x1) - funktion.subs(x, x0)))
            * funktion.subs(x, x1),
            x1,
        )
        print(f"x_{i} = {x0} -> {x1}")
    return x1


# Beispiel mit 2 Funktionen die einen Schnittpunkt haben
x = symbols("x")
funktion1 = (x**2 + 1) ** 2 - 10
funktion2 = 5 / ((x - 1) ** 2 + 1)
funktion = funktion1 - funktion2

sekanteverfahren_anzahl_iterationen(funktion, 1.6, 1.7, 2)
