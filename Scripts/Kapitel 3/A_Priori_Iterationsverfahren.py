import numpy as np
from sympy import diff, exp, symbols, log


# Das Alpha, welches beim 2. Schritt vom Banach berechnet wird. Auch genannt Lipschitz-Konstante L.
def getAlpha(funktion, start, end):
    y = diff(funktion, x)
    y_werte = np.array([])
    for i in np.arange(start, end + 0.1, 0.1):
        y_werte = np.append(y_werte, y.subs(x, i).evalf())

    print("α = ", np.max(np.abs(y_werte)))
    return y_werte.max()


def a_priori_mit_bekannter_toleranz(alpha, x0, x1, tol):
    iterationen = log((tol * (1 - alpha)) / np.abs(x1 - x0)) / log(alpha)
    print(
        f"Anzahl Iterationsschritte mit Toleranz {tol}: {iterationen} bzw. {round(iterationen)}"
    )


x = symbols("x")
funktion = exp(x)
start_intervall = -3
end_intervall = -2
alpha = getAlpha(funktion, start_intervall, end_intervall)

# Funktion mit x0 eingesetzt bzw 1 Iterationsschritt
x1 = np.exp(-2.5) - np.exp(1)
a_priori_mit_bekannter_toleranz(alpha, -2.5, x1, 10**-5)

# Andere Beispiele aus den Aufgaben
# x = symbols("x")
# funktion = (230 * x**4 + 18 * x**3 + 9 * x**2 - 9) / 221
# alpha = getAlpha(funktion, -0.5, 0.5)
# a_priori_mit_bekannter_toleranz(alpha, 0, -0.0407239819004525, 10**-9)

# a_priori_mit_bekannter_toleranz(0.75, 0.3, 0.6, 10**-8)
