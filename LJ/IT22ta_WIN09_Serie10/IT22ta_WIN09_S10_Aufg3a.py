import math
import numpy.linalg as lin
import numpy as np
from sympy import false, true

def IT22ta_WIN09_S10_Aufg3a (A, b, x0, tol, opt):
    
    xStart = x0
    D = np.diag(np.diag(A))
    R = np.triu(A) - D
    L = np.tril(A) - D
    A = 0
    Inv = lin.inv(D)
    n = 1
    #Jacobi-Verfahren
    if (opt):
        #Speicherplatz freigeben
        D = 0
        xn = -Inv@(L + R)@x0 + Inv@b
        x1 = xn
        B = -Inv@(L + R)
        while (lin.norm(xn - x0, np.inf) > tol):
                x0 = xn
                xn = -Inv@(L + R)@x0 + Inv@b
                n += 1

        

    #Gauss-Seidel-Verfahren 
    else:
         InvDL = lin.inv(D + L) 
         xn = -InvDL@R@x0 + InvDL@b 
         x1 = xn
         B = -InvDL@R
         
         while (lin.norm(xn - x0, np.inf) > tol):
                x0 = xn
                xn = -InvDL@R@x0 + InvDL@b 
                n += 1
         
    #Speicherplatz freigeben
    L = 0
    R = 0

    priori = lin.norm(B, np.inf)
    p = tol / lin.norm(x1 - xStart, np.inf)
    p = p * (1 - priori)

    n2 = np.log(p) / np.log(priori)
    n2 = math.ceil(n2)

    return (xn, n, n2)


#Initialwerte setzen
A = np.array([[8,5,2], [5, 9, 1], [4, 2, 7]])
b = np.array([19, 5, 34])
x0 = np.array([1, -1, 3])
tol = 10**(-4)
opt = false

#Jacobi-Verfahren
[xn, n, n2] = IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, true)
print("xn: {}, n: {}, n2: {}".format(xn, n, n2))
#Gauss-Seidel-Verfahren
[xn, n, n2] = IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, false)
print("xn: {}, n: {}, n2: {}".format(xn, n, n2))