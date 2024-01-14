def anz_verschied_maschinZahlen(basis, mantisse, exponent, vorzeichen_exp):
    return basis ** (mantisse) * (basis ** (exponent + vorzeichen_exp) - 1) + 1


########################################################################################

# Basis
basis = 2

# Anzahl Stellen für Mantisse
mantisse_stellen = 15

# Anzahl Stellen für Exponent
exponent_stellen = 5

# Vorzeichen (Ja = 1, Nein = 0)
vorzeichen = 1

print(
    anz_verschied_maschinZahlen(basis, mantisse_stellen, exponent_stellen, vorzeichen)
)
