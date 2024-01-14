import numpy as np
from IT22ta_WIN09_S6_Aufg2 import obereDreiecksMatrix

A1 = np.array([[-1, 1, 1], [1, -3, -2], [5, 1, 4]])
c1 = np.array([13, -32, 22])

[triangle, det, x1] = obereDreiecksMatrix(A1, c1)

x2 = np.linalg.solve(A1, c1)

print(
    "Das Resultat mit unserer Berechnung lautet {}. Das Resultat mit numpy.linalg.solve() lautet: {}. det: {}".format(
        x1, x2, det
    )
)

A1 = np.array([[4, -1, -5], [-12, 4, 17], [32, -10, -41]])
b1 = np.array([6, -12, 48])

[triangle, det, x1] = obereDreiecksMatrix(A1, b1)

x2 = np.linalg.solve(A1, b1)

print(
    "Das Resultat mit unserer Berechnung lautet {}. Das Resultat mit numpy.linalg.solve() lautet: {}. det: {}".format(
        x1, x2, det
    )
)

A1 = np.array([[2, 7, 3], [-4, -10, 0], [12, 34, 9]])
b1 = np.array([5, -22, 42])

[triangle, det, x1] = obereDreiecksMatrix(A1, b1)

x2 = np.linalg.solve(A1, b1)

print(
    "Das Resultat mit unserer Berechnung lautet {}. Das Resultat mit numpy.linalg.solve() lautet: {}. det: {}".format(
        x1, x2, det
    )
)

A1 = np.array([[-2, 5, 4], [-14, 38, 22], [6, -9, -27]])
b1 = np.array([16, 82, -120])

[triangle, det, x1] = obereDreiecksMatrix(A1, b1)

x2 = np.linalg.solve(A1, b1)

print(
    "Das Resultat mit unserer Berechnung lautet {}. Das Resultat mit numpy.linalg.solve() lautet: {}. det: {}".format(
        x1, x2, det
    )
)

A1 = np.array(
    [
        [-1, 2, 3, 2, 5, 4, 3, -1],
        [3, 4, 2, 1, 0, 2, 3, 8],
        [2, 7, 5, -1, 2, 1, 3, 5],
        [3, 1, 2, 6, -3, 7, 2, -2],
        [5, 2, 0, 8, 7, 6, 1, 3],
        [-1, 3, 2, 3, 5, 3, 1, 4],
        [8, 7, 3, 6, 4, 9, 7, 9],
        [-3, 14, -2, 1, 0, -2, 10, 5],
    ]
)
c1 = np.array([-11, 103, 53, -20, 95, 78, 131, -26])


[triangle, det, x1] = obereDreiecksMatrix(A1, c1)

x2 = np.linalg.solve(A1, c1)

print(
    "Das Resultat mit unserer Berechnung lautet {}. Das Resultat mit numpy.linalg.solve() lautet: {}. det: {}".format(
        x1, x2, det
    )
)

# Für kleine Matrizen gibt es keine Unterschiede zwischen unserer Methode und der von numpy. Für die oben angegebene 8x8 Matrix jedoch gibt es einen Unterschied.
# Mit numpy.linalg.solve() erhalten wir: 2.12233332e-15, und mit unserer Methode erhalten wir: 5.81353147e-14. Dies kommt daher, dass wir nicht mit der
# Pivotisierung arbeiten und die Methode von numpy schon.
