import numpy as np
from IT22ta_WIN09_S6_Aufg2 import obereDreiecksMatrix

A1 = np.array([[-1,1,1],[1,-3,-2],[5,1,4]], dtype=float)
c1 = np.array([13,-32,22], dtype=float)

A2 = np.copy(A1)
c2 = np.copy(c1)

[triangle, det, x1] = obereDreiecksMatrix(A1,c1)

x2 = np.linalg.solve(A2,c2)

print("Das Resultat mit unserer Berechnung lautet {}. Das Resultat mit numpy.linalg.solve() lautet: {}".format(x1,x2))

# Für die oben angegebene Matrix  und c lautet x = [-1,7,5] für beide Rechenwege. Es gibt keine Unterschiede.