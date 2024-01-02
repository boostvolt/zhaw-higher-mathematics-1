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


########################################################################################

# Funktion definieren
funktion = "exp(x) - exp(1)"

# Wert für x_0 definieren
x_0 = {"x": -2.5}

# Intervall definieren
interval = [-3, -2]

# Toleranz definieren
toleranz = 10**-5

print(f"α = {get_alpha(funktion, interval)}")
print(
    f"Anzahl Iterationsschritte: {a_priori_mit_bekannter_toleranz(get_alpha(funktion, interval), x_0[list(x_0.keys())[0]], sympify(funktion).subs(x_0).evalf(), toleranz)}"
)

# Andere Beispiele aus den Aufgaben
# Beispiel 1
# funktion = "(230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221"
# werte = {"x": 0}
# interval = [-0.5, 0.5]
# toleranz = 10**-9

# Beispiel 2
# funktion = "sqrt(1 - x)"
# werte = {"x": 0.5}
# interval = [0.5, 0.71]
# toleranz = 10**-6

# Beispiel 3
# funktion = "2 * exp(-x / 2)"
# werte = {"x": 0.8}
# interval = [0.8, 1.4]
# toleranz = 10**-6
