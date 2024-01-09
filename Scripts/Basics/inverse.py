import numpy as np 

# Matrix definieren
A = np.array([[4, 1, 0], [3, 2, 1], [5, 2, -1]])

print('Die Inverse von ${} lautet: ${}'.format(A,np.linalg.inv(A)))