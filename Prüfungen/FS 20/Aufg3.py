# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:37:39 2020

SEP FS20 Aufgabe 3

@author: knaa
"""
import numpy as np
import matplotlib.pyplot as plt

N = 100
epsIncr = 1e-6

xL = 1
xR = 2


def F(x):
    return 1.0 / (np.cos(x + np.pi / 4) - 1) + 2


def dF(x):
    return np.sin(x + np.pi / 4) / (np.cos(x + np.pi / 4) - 1) ** 2


# Achtung: die Ableitung konnte damals mit Matlab berechnet werden. In Python sind wir noch nicht so weit.
# Allerdings ist auch die Berechnung der Ableitung von Hand nicht wirklich schwer.

# Aufgabe a)
print("\nFixpunktiteration a)\n")

xPlot = np.arange(0, np.pi + 0.01, 0.01)
plt.figure(1)
plt.plot(
    xPlot,
    xPlot,
    xPlot,
    F(xPlot),
    xPlot,
    np.abs(dF(xPlot)),
    [xL, xL],
    [0, np.pi],
    "k-.",
    [xR, xR],
    [0, np.pi],
    "k-.",
)
plt.legend(["y=x", "y=F(x)", "y=abs(F'(x))"])
plt.axis([0, np.pi, 0, np.pi])

# Aufgabe b)
print("\nFixpunktiteration b)\n")

fx = F(np.array([xL, xR]))
fxMin = np.min(fx)
fxMax = np.max(fx)
dfx = dF(np.array([xL, xR]))
lambd = np.max(np.abs(dfx))

print(lambd < 1)
print(fxMin > xL)
print(fxMax < xR)
# Banach erfüllt, wenn 3 x logisch 1

# Aufgabe c)
print("\nFixpunktiteration c)\n")
lambd
xj = 1.3376
xj1 = 1.3441
errEst = lambd / (1 - lambd) * (xj1 - xj)

# Verbesserung von lambda (da Graph von dF monoton abnehmend)
xj = 1.3376
xj1 = 1.3441
lambdaEst = dF(xj)
errEst = lambdaEst / (1 - lambdaEst) * (xj1 - xj)

# Aufgabe d)
print("\nFixpunktiteration d)\n")


def fixIt(f, x0, epsIncr, lambd):
    import numpy as np

    k = 0
    notConverged = True
    N = 1000

    x0
    while notConverged and k < N:
        x1 = f(x0)
        incr = np.abs(x1 - x0)
        error = lambd / (1 - lambd) * incr
        notConverged = error > epsIncr
        k = k + 1
        x0 = x1
    n = k
    return (x1, n)


x0 = 1
[xF, n] = fixIt(F, x0, epsIncr, lambd)
print("xF=%.4E" % xF, "(n=%.4E Iterationen)\n" % n)

# Aufgabe e)
print("\nFixpunktiteration e)\n")


def fA(x):
    return (x - 1) / (x - 2) - np.cos(x + np.pi / 4)


def fB(x):
    return F(x)


def fC(x):
    return x + (2 - 1 / (np.cos(x + np.pi / 4) - 1))


def fD(x):
    return np.cos(x + np.pi / 4) - 1 / (x - 2) - 1


print("A ist ", np.abs(fA(xF)) < 1e-6)
print("B ist ", np.abs(fB(xF)) < 1e-6)
print("C ist ", np.abs(fC(xF)) < 1e-6)
print("D ist ", np.abs(fD(xF)) < 1e-6)
# d.h. korrekt ist A) und D)
