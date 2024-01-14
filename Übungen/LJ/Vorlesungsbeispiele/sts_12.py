import numpy as np

# Datenliste
data = np.array([[1, 3], [-5, -3], [-3, 3], [0, -1], [-2, 2]])

# x und y Werte
x = data[:, 0]
y = data[:, 1]

# Regressionsgerade (nach y)
a_y = np.corrcoef(x, y)[0, 1] * np.std(y) / np.std(x)
b_y = np.mean(y) - a_y * np.mean(x)

# Residuenvarianz
residuals = y - (a_y * x + b_y)
residual_variance = np.var(residuals)

# Totale Varianz
total_variance = np.var(y)

# Erklärte Varianz
explained_variance = total_variance - residual_variance

# Bestimmtheitsmass
r_squared = explained_variance / total_variance

# Pearson Korrelationskoeffizient
pearson_corr = np.corrcoef(x, y)[0, 1]

# Regressionsgerade (nach x)
a_x = np.corrcoef(y, x)[0, 1] * np.std(x) / np.std(y)
b_x = np.mean(x) - a_x * np.mean(y)

# Ausgabe der berechneten Werte
print(f"Regressionsgerade (nach y): y(x) = {a_y:.2f} * x + {b_y:.2f}")
print(f"Residuenvarianz: {residual_variance:.2f}")
print(f"Erklärte Varianz: {explained_variance:.2f}")
print(f"Totale Varianz: {total_variance:.2f}")
print(f"Bestimmtheitsmass: {r_squared:.2f}")
print(f"Pearson Korrelationskoeffizient: {pearson_corr:.2f}")
print(f"Regressionsgerade (nach x): x(y) = {a_x:.2f} * y + {b_x:.2f}")
