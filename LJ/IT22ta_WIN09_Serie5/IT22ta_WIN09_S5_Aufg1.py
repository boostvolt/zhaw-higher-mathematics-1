import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2
# a)
# Anziehende Fixpunkte für die folgenden Input-Werte mit 100 Iterationen:
# 0, 1.5, 2.0, 2.5
# Für Werte folgende Werte liegt ein abstossender Fixpunkt vor mit 100 Iterationen:
# 0.5, 1.0, 3.0, 3.5, 4.0

# b)
# Für Werte nahe beim Fixpunkt kann ausgesagt werden, dass die Krankheitszahlen stagnieren.
# Für Werte kleiner als der Fixpunkt kann gesagt werden, dass mehr gesund sind als krank werden.
# Für Werte grösser als der Fixpunkt kann gesagt werden, dass mehr Leute infiziert werden als gesund sind.

#c)
# alpha = k_(i+1) / (k_i*(1-k_i))
# Der Fixpunkt wird dann erreicht, wenn k_i und k_(i+1) den gleichen Wert annehmen.
# Daraus folgt alpha = 1 / (1 - k_i)
# Unser Fixpunkt entspricht demnach k_1 = 1 - (1/alpha)

def K (alpha,k):
    return alpha * k * (1-k)

def fixpunkt(alpha,k,loop):

    if loop > 0:

        print("{}: {}".format(alpha, K(alpha,k)))
        fixpunkt(alpha,K(alpha,k),loop-1)

k0 = 0.1
alpahrange = np.arange(0,4.1,0.5)

for x in alpahrange:

    fixpunkt(x,k0,100)
    print("-------")