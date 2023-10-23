import numpy as np

def sekantenVerfahren(f, x0,x1,tol):
    res = 0
    while (np.abs(x1-x0) > tol):
        res = x1 - ((x1-x0)/(f(x1)-f(x0))) * f(x1)
        x0 = x1
        x1 = res

    return res
    

def f1(x):
    return (np.e) ** (x**2) + (x ** (-3)) -10

def f2(x): 
    return (-1/3)*(np.pi * (x ** 3)) + (5 * np.pi * (x ** 2)) - 471

print("Überprufung Aufgabe 1:")
print(sekantenVerfahren(f1, -1,-1.2, 10 ** (-3)))

print("Überprufung Aufgabe 2:")
print(sekantenVerfahren(f2, 8.5,9.5, 10 ** (-3)))

# Wir haben mit unserer Mehode dieselben Resultate erhalten, wie wir zuvor von Hand ausgerechnet haben.

# Beim Versuch das Newton-Verfahren zu implementieren würden wir auf Probleme bei der Ableitung von f stossen. Wir müssten 
# die verschiedenen Ableitungen von f berechnen, bevor wir überhaupt die Nullstellen berechnen könnten.