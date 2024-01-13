from sympy import Matrix, symbols

# Definieren Sie unbekannte Variablen
x, y = symbols("x y")

# Erstellen Sie Matrizen mit unbekannten Variablen
A = Matrix([[-0.166666666666667 * x], [-30], [-0.1 * x]])

# Ein Vektor wird auch mit Matrix() erstellt!
B = Matrix([1 / 6 * x, 1, 1 / 10 * x])

# Führen Sie eine Matrizenaddition durch
C = A + B

# Zeigen Sie das Ergebnis an
if C.shape[0] == 1 or C.shape[1] == 1:
    # Es ist ein Vektor
    print("Vektor:")
    print(C)
else:
    # Es ist eine Matrix
    print("Matrix:")
    print(C)
