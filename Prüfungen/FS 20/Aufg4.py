# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:29:47 2020

SEP FS20 Aufgabe 4

@author: knaa
"""

import numpy as np

# Aufgabe a)
A = np.array([[15, 0, 1], [1, 3, 7], [0, 1, 6]])
y = np.array([[21, 67, 44]]).T


""" 
Die 1. und 2. Zeile müssen vertauscht werden, da ansonsten ein
Diagonal-Element 0 ist und die Diagonaldominanz nicht mehr gegeben ist ! 
"""

D = np.diag(np.diag(A))
R = np.triu(A) - D
L = np.tril(A) - D

# Aufgabe b)

x = np.array([[0, 0, 0]]).T

for k in np.arange(1, 7):
    x = -np.linalg.inv(D + L) @ R @ x + np.linalg.inv(D + L) @ y
    print(x)


# Aufgaben c)

"""
Bei grossen Gleichungssystemen ist der numerische Aufwand von exakten
Lösungsverfahren zu gross. Iterative Verfahren sind bei solchen
(insbesondere diagonal dominanten) Gleichungsystemen effizienter
"""
