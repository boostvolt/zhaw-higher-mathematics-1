# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:11:45 2020

SEP FS20 Aufgabe 2

@author: knaa
"""

# a)
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x * np.exp(x)


def df(x):
    return np.exp(x) * (x + 1)


def K(x):
    return np.abs(x) * np.abs(df(x)) / np.abs(f(x))


# K = abs(x + 1)
x = np.arange(-4, 2.05, 0.05)
plt.plot(x, K(x), "-"), plt.xlabel("x"), plt.ylabel("K(x)")

# b)
"""
Gut konditioniertes Problem fuer K <= 1        

Forderung: |x+1| <= 1    

Fuer x > -1: 
  Forderung: 1 + x <= 1 
    => x <= 0                                  2P
Fuer x < -1:
  Forderung: -(1+x) <= 1
    => -1-x <= 1
    => -x <= 2
    => x >= -2                                 2P
    
Gute Konditionierung fuer -2 <= x <= 0         1P

"""
