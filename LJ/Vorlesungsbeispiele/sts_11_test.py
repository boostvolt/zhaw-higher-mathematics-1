import math
from scipy.stats import norm


def calculate_probability(n, a, b, target_sum):
    # Berechne die Varianz der Gleichverteilung
    variance = ((b - a) * (b - a + 2)) / 12

    # Berechne den Mittelwert und die Standardabweichung der Summe
    mean_sum = n * (a + b) / 2
    std_dev_sum = math.sqrt(n * variance)

    # Standardisiere die Zufallsvariable
    z = (target_sum - mean_sum) / std_dev_sum

    # Verwende die Standardnormalverteilungstabelle, um die Wahrscheinlichkeit zu berechnen
    probability = norm.cdf(z)

    return probability


# Parameter: Anzahl der generierten Zahlen, Bereich (a, b), Zielsumme
n = 113
a = 6
b = 15
target_sum = 1186

# Berechne die Wahrscheinlichkeit
result_probability = calculate_probability(n, a, b, target_sum)

print(
    f"Die Wahrscheinlichkeit, dass die Summe größer als {target_sum} ist, beträgt etwa {result_probability:.4f}"
)
