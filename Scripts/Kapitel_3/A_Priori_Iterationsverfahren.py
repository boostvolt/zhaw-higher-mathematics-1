import numpy as np
from sympy import diff, log, sympify


# Das Alpha, welches beim 2. Schritt vom Banach berechnet wird. Auch genannt Lipschitz-Konstante L.
def get_alpha(funktion, interval):
    funktion = sympify(funktion)
    symbols = list(funktion.free_symbols)

    if len(symbols) == 0:
        raise ValueError("Keine Unbekannte in Funktion gefunden.")

    if len(interval) != 2:
        raise ValueError("Intervall muss aus zwei Werten bestehen.")

    y_werte = np.array([])
    for i in np.linspace(interval[0], interval[1], 100):
        y_werte = np.append(
            y_werte, diff(funktion, symbols[0]).subs(symbols[0], i).evalf()
        )

    return np.max(np.abs(y_werte))


def a_priori_mit_bekannter_toleranz(alpha, x_0, x_1, toleranz):
    return log((toleranz * (1 - alpha)) / (np.abs(x_1 - x_0))) / log(alpha)


# Funktion definieren
funktion = "exp(x) - exp(1)"

# Werte für Unbekannte definieren
werte = {"x": -2.5}

# Intervall definieren
interval = [-3, -2]

# Toleranz definieren
toleranz = 10**-5

print(f"α = {get_alpha(funktion, interval)}")
print(
    f"Anzahl Iterationsschritte: {a_priori_mit_bekannter_toleranz(get_alpha(funktion, interval), werte['x'], sympify(funktion).subs(werte).evalf(), toleranz)}"
)

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

# Beispiel 3
# x = symbols("x")
# funktion = 2 * exp(-x / 2)
# start_intervall = 0.8
# end_intervall = 1.4
# alpha = getAlpha(funktion, start_intervall, end_intervall)

# # Funktion mit x0 eingesetzt um x1 zu bekommen
# x1 = funktion.subs(x, 0.8)
# print(x1)
# a_priori_mit_bekannter_toleranz(alpha, 0.8, x1, 10**-6)
