def maschinengenauigkeit(basis, mantisse_stellen):
    return (basis / 2) * basis ** (-mantisse_stellen)

# Werte für Basis B und Anzahl Mantisse-Stellen definieren
basis = 10
mantisse_stellen = 2

print(f"Maschinengenauigkeit eps: {maschinengenauigkeit(basis, mantisse_stellen)}")