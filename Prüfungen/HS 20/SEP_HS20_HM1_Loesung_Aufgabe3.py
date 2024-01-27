import numpy as np


def g(x):
    return np.exp(x)


def h(x):
    return np.sqrt(x) + 2


# a) 5P


def f(x):
    return g(x) - h(x)


def df(x):
    return np.exp(x) - 0.5 / np.sqrt(x)


x0 = 0.5
tol = 1e-7
err = 1 + tol
niter = 0
while err > tol:
    x1 = x0 - f(x0) / df(x0)
    err = np.abs(x1 - x0)
    x0 = x1
    niter += 1
print("Schnittpunkt=", x0, ", niter=", niter)
# Schnittpunkt= 1.1174679154114777

# b) 5P


# 1.
# exp(x) = sqrt(x) + 2 => x = ln(sqrt(x) + 2) =: F(x)
def F(x):
    return np.log(np.sqrt(x) + 2)


# 2. F(x) ist monoton zunehmende Funktion
# [a,b] = [0.5,1.5]
a = 0.5
b = 1.5
print("F(a)=", F(a), ", F(b)=", F(b))

print(a < F(a) and F(b) < b)
# F(a) = 0.996 > 0.5
# F(b) = 1.171 < 1.5
# => F ist Selbstabb.

# |F'(x)| = 1/((sqrt(x)+2)*2*sqrt(x)) ist fuer 0 < x monoton abnehmend
# => L = max |F'(x)| = |F'(a)| = 0.2612 < 1
# => F ist Kontraktion

# 3. A-priori
L = 1 / ((np.sqrt(a) + 2) * 2 * np.sqrt(a))
print("L=", L)
x0 = 0.5
x1 = F(x0)
tol = 1e-7
n = np.log(tol * (1 - L) / np.abs(x1 - x0)) / np.log(L)
print("n=", n)
# n = 11.709 => n = 12 Schritte


"""
err = 1+tol
m = 0
while err>tol:
    x1 = F(x0)
    err = np.abs(x1-x0)*L/(1-L)
    x0 = x1
    m += 1
    
print('x0=', x0,'m=',m)
"""

"""
# Plot fuer Pruefungsblatt
import matplotlib.pyplot as plt

x = np.linspace(0,2)

plt.plot(x,g(x),'-k',label='g(x)')
plt.plot(x,h(x),'--k',label='h(x)')
plt.legend()
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#plt.savefig('fig_nonlin_a.png')
"""
