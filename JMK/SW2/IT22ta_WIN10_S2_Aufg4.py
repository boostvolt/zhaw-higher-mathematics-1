# Aufgabe 4 a)
def eps():
    n = 1
    while 1 + 2 ** (-n) != 1:
        n += 1

    return 2 ** (-n)


print(eps())

## Maschinengenauigkeit des Rechners beträgt 1.1102230246251565e-16, also 16 Nachkommmastellen


# Aufgabe 4 b)
def qmin():
    n = 1.0
    while 1 + (2**n) != (2**n):
        n += 1

    return 2**n


print(qmin())
## qmin beträgt 9007199254740992.0 und ist auch 16 Stellen lang wie die Maschinengenauigkeit
