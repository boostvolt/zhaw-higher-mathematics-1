from math import ceil

import numpy as np
from sympy import diff, exp, log, symbols


# Das Alpha, welches beim 2. Schritt vom Banach berechnet wird. Auch genannt Lipschitz-Konstante L.
def getAlpha(funktion, start, end):
    y = diff(funktion, x)
    y_werte = np.array([])
    for i in np.linspace(start, end, 100):
        y_werte = np.append(y_werte, y.subs(x, i).evalf())

    print("α = ", np.max(np.abs(y_werte)))
    return np.max(np.abs(y_werte))


def a_priori_mit_bekannter_toleranz(alpha, x0, x1, tol):
    iterationen = log((tol * (1 - alpha)) / (np.abs(x1 - x0))) / log(alpha)
    print(
        f"Anzahl Iterationsschritte mit Toleranz {tol}: {iterationen.evalf()} bzw. {ceil(iterationen.evalf())}"
    )


x = symbols("x")
funktion = exp(x) - exp(1)
start_intervall = -3
end_intervall = -2
alpha = getAlpha(funktion, start_intervall, end_intervall)

# Funktion mit x0 eingesetzt um x1 zu bekommen
x1 = funktion.subs(x, -2.5)
a_priori_mit_bekannter_toleranz(alpha, -2.5, x1, 10**-5)

# Andere Beispiele aus den Aufgaben

# Beispiel 1
# x = symbols("x")
# funktion = (230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221
# alpha = getAlpha(funktion, -0.5, 0.5)
# a_priori_mit_bekannter_toleranz(alpha, 0, -0.0407239819004525, 10**-9)

# Beispiel 2
# x = symbols("x")
# funktion = sqrt(1 - x)
# start_intervall = 0.5
# end_intervall = 0.71
# alpha = getAlpha(funktion, start_intervall, end_intervall)

# x0 = 0.5
# x1 = funktion.subs(x, x0)
# toleranz = 10**-6
# a_priori_mit_bekannter_toleranz(alpha, x0, x1, toleranz)
