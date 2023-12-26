import matplotlib.pyplot as plt
import numpy as np

# 100 Werte für x von 0 bis 1 gleichmässig verteilt
x = np.linspace(0, 1, 100)
# Werte für x eingeben 0 bis 1 mit Schrittlänge 0.1
#x = np.arange(0, 1, 0.1)
f1 = (x + np.log(x))
#f2 = (x - 2) ** 7

plt.plot(x, f1)
# Mehrere Funktionen im gleichen Plot darstellen
#plt.plot(x, f2)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Polynomial")
# Legende für mehrere Funktionen im gleichen Plot
#plt.legend(["f1(x)", "f2(x)"])
plt.legend(["f1(x)"])
# Wertebereich für x-Achse definieren
#plt.xlim(0,1)
# Wertebereich für y-Achse definieren
#plt.ylim(0,1)
plt.grid()
plt.show()