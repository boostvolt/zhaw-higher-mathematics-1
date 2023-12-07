import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2 a)
x = np.linspace(1.99, 2.01, 501)
f1 = (
    x**7
    - 14 * x**6
    + 84 * x**5
    - 280 * x**4
    + 560 * x**3
    - 672 * x**2
    + 448 * x
    - 128
)
f2 = (x - 2) ** 7
plt.figure()
plt.plot(x, f1)
plt.plot(x, f2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Aufgabe 2 a)")
plt.legend(
    [
        "x^7 - 14x^6 + 84x^5 - 280x^4 + 560x^3 - 672x^2 + 448x - 128",
        "(x - 2)^7",
    ]
)
plt.show()
## Bei der Funktion F1 werden die Rundungsfehler bei der Addition und Subtraktion bei jeder erneuten Multiplikation erneut mit einberechnet und daher vergrössert.
## Die Unterschiede sind auf numerischen Rundungsfehler zurückzuführen die beim berechnen und darstellen von Fliesskommazahlen in Python auftreten können.
## Aufgrund von Rundungsfehler, rechnet die Funktion f1 mit diesen Rundungsfehler immer weiter und addieren sich.
## Die Funktion f2 rechnet mit dem Binomischen Lehrsatz und ist somit genauer.

# Aufgabe 2 b)
x2 = np.arange(-(10**-14), 10**-14, 10**-17)
g = x2 / (np.sin(1 + x2) - np.sin(1))
plt.figure()
plt.plot(x2, g)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Aufgabe 2 b)")
plt.legend(
    [
        "x / (sin(1 + x) - sin(1)))",
    ]
)
plt.show()
## Nein, die Werte variieren sehr stark, weswegen sich im Plot "Zacken" bilden.

# Aufgabe 2 c)
# g2 = x2 / (2 * np.cos(((1 + x2) + 1) / 2) * np.sin(((1 + x2) - 1) / 2))
g2 = x2 / ((2 * np.cos((2 + x2) / 2)) * np.sin(x2 / 2))
plt.figure()
plt.plot(x2, g2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Aufgabe 2 c)")
plt.grid()
plt.legend(
    [
        "x / 2(2 * cos((2 + x) / 2)) * sin(x / 2))",
    ]
)
plt.ylim(1, 2)
plt.show()

# Der Grenzwert beträgt 1.81 weil es keine Division durch Null mehr gibt.
