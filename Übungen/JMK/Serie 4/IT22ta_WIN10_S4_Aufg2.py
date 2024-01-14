import numpy as np


def fix_point_iteration(alpha, k):
    return alpha * k * (1 - k)


k0 = 0.1
alpha_values = np.arange(0, 8.1, 0.5)
for alpha in alpha_values:
    k = k0
    print(f"alpha = {alpha}")
    for i in range(21):
        k = fix_point_iteration(alpha, k)
        print(f"k = {k}")

# Aufgabe 2
# a) Ab 21 Iteration haben alpha 0, 1.5, 2, 2.5 einen Fixpunkt.
# b) Der Fixpunkt gibt an bei welcher Infektionsrate die Anzahl erkrankten und gesunden Kindern stagniert. (Gleich viele gesund wie krank)
