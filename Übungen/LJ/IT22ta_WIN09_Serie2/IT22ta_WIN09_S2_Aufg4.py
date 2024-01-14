eps = 1.0

while 1.0 + eps != 1.0:
    eps /= 2.0

print("Maschinengenauigkeit (eps) beträgt:", eps)

# Auf beiden Rechnern erhalten wir folgendes Resultat: Maschinengenauigkeit (eps) beträgt: 1.1102230246251565e-16
# Dies bedeutet: wir haben eine Maschinengenauigkeit von 16 signifikanten Dezimalstellen.

q_min = 1.0

while 1.0 + q_min != q_min:
    q_min *= 2.0

print("Maschinengenauigkeit (q_min) beträgt:", q_min)

# Wir erhalten ein q_min von: 9007199254740992.0
# Diese Zahl hat ebenfalls 16 signifikante Stellen.
# Sowohl q_min und 1 als auch eps und 1 liegen also 16 Stellen auseinander.
