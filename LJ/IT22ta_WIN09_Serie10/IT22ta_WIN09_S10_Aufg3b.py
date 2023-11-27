import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as lin
import timeit

from sympy import false, true
from IT22ta_WIN09_S10_Aufg3a import IT22ta_WIN09_S10_Aufg3a
from IT22ta_WIN09_S6_Aufg2 import obereDreiecksMatrix


dim = 3000
A = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))
print(A)
dum1 = np.arange(1,int(dim/2+1),dtype=np.float64).reshape((int(dim/2),1)) 
dum2 = np.arange(int(dim/2),0,-1,dtype=np.float64).reshape((int(dim/2),1)) 
x = np.append(dum1,dum2,axis=0)

b = A@x
x0 = np.zeros((dim,1))
tol = 1e-4
opt = false

#t3=timeit("Serie8_Aufg2(Test)", "from __main__ import Serie8_Aufg2, Test") 
#t4=timeit("np.linalg.qr(Test)", "from __main__ import np, Test")
#t1 = timeit.timeit("IT22ta_WIN09_S10_Aufg3a(A, b, x0, tol, opt)", "from __main__ import IT22ta_WIN09_S10_Aufg3a, A, b, x0, tol, opt")
#t2 = timeit.timeit(lambda: np.linalg.solve(A, b), number=1)
#t3 = timeit.timeit("np.linalg.solve(A, b)", "from __main__ import np, A, b")
#print(t2)
