import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2
# a)
# Für Werte von 0 bis 2.5 mit Abstand 0.5 liegt ein anziehender Fixpunkt vor.
# Für Werte von 3.0 bis 4.0 liegt ein abstossender Fixpunkt vor.

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

    fixpunkt(x,k0,30)
    print("-------")