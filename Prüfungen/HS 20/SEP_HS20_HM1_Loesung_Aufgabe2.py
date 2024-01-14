# ------------------------------------------------------------
# SEP HS20 HM1 / LOESUNG AUFGABE 2 / adel
# ------------------------------------------------------------

# TEILAUFGABE a)

#          f'(x)*x       (2*x*sin(x)+x^2*cos(x))*x
# K(x) = |---------| = |---------------------------|
#            f(x)              x^2*sin(x)
#
#          2*sin(x)+x*cos(x)
#      = |------------------|
#               sin(x)                                     1 P
#        ===================

# TEILAUFGABE b)

# Naeherungsweise gilt
#
# |(f(x)-f(x0))/f(x0)| = K(x0)*|(x-x0)/x0|               0.5 P
#
# Aus |(f(x)-f(x0))/f(x0)| <= 0.1 folgt
#
# |x-x0| <= 0.1/K(x0)*x0                                   1 P

import numpy as np


def K(x):
    return np.abs((2 * np.sin(x) + x * np.cos(x)) / np.sin(x))


x0 = np.pi / 3
y0_err_rel = 0.1
x0_err_abs = y0_err_rel / K(x0) * x0
print(x0_err_abs)
# 0.040205699009494354 = 0.04021                         1.5 P
#                        =======

# TEILAUFGABE c)

print([K(10**-n) for n in range(1, 6)])
# [2.9966644423259243,
#  2.999966666444442,
#  2.999999666666645,
#  2.9999999966666664,
#  2.9999999999666667]                                     2 P

# Fuer x -> 0 konvergiert K(x) -> 3. Dementsprechend
# ist f(x) in x = 0 gut konditioniert.
# ==================================================       1 P

# TEILAUFGABE d)

import matplotlib.pyplot as plt

x = np.arange(-2 * np.pi, 3 * np.pi, 10**-4)
plt.semilogy(x, K(x))
plt.xlabel("x")
plt.ylabel("K(x)")
plt.grid()  #   2 P

# Der Plot zeigt, dass f(x) fuer x in der Umgebung von +/- pi,
# +/- 2*pi, +/- 3*pi, usw. schlecht konditioniert ist.
# ===================================================       1 P
