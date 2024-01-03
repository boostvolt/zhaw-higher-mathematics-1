def maschinengenauigkeit(basis, mantisse_stellen):
    return (basis / 2) * basis ** (-mantisse_stellen)


########################################################################################

# Wert für Basis B definieren
basis = 10

# Anzahl der Mantisse-Stellen
mantisse_stellen = 2

print(f"Maschinengenauigkeit eps: {maschinengenauigkeit(basis, mantisse_stellen)}")
