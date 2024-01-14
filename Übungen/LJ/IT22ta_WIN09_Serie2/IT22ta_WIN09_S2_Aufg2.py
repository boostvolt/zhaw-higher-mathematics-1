import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1.99, 2.01, 501)
f1 = (
    (x**7)
    - (14 * (x**6))
    + (84 * (x**5))
    - (280 * (x**4))
    + (560 * (x**3))
    - (672 * (x**2))
    + 448 * x
    - 128
)
f2 = (x - 2) ** 7

plt.plot(x, f1)
plt.plot(x, f2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Polynomial")
plt.legend(["f1(x)", "f2(x)"])
plt.grid()
plt.show()

# Bei der Funktion f1 werden die Rundungsfehler bei der Addition und Subtraktion
# bei jeder erneuten Multiplikation erneut miteinberechnet und daher vergrössert.
# Die Unterschiede, die wir sehen sind auf numerische Rundungsfehler zurückzuführen,
# die beim Berechnen und Darstellen von Fliesskommawerten in Python auftreten können.

x = np.arange(-1e-14, 1e-14, 1e-17)
g = x / (np.sin(1 + x) - np.sin(1))
plt.plot(x, g)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Polynomial")
plt.legend(["g(x)"])
plt.grid()
plt.show()

# Es ist wichtig zu beachten, dass die Schrittweite von 10^(-17) in einem so kleinen Intervall
# wie [-10^(-14), 10^(-14)] problematisch sein kann,
# da Sie möglicherweise nicht genügend äquidistante Punkte innerhalb dieses Intervalls generieren können,
# aufgrund der begrenzten Genauigkeit von Gleitkommazahlen in Python.
# Python wird möglicherweise nicht in der Lage sein, äquidistante Werte im Intervall zu generieren,
# die kleiner sind als die kleinste darstellbare Gleitkommazahl.
# Die Funktion ist instabil, wie anhand der sprunghaften Richtungsänderungen des Graphen zu erkennen ist.

g1 = x / ((2 * np.cos((2 + x) / 2)) * np.sin(x / 2))
plt.ylim(-2, 2)
plt.plot(x, g1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Polynomial")
plt.legend(["g(x)"])
plt.grid()
plt.show()

# Weil die Division durch Null eliminiert wurde ist die Funktion nun stabil und der Wert beträgt 1.85.
