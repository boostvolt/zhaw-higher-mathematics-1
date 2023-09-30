import numpy as np
import matplotlib.pyplot as plt
import timeit


def fact_rec(n):
# y = fact_rec(n) berechnet die Fakultät von n als fact_rec(n) = n * fact_rec(n -1) mit fact_rec(0) = 1
# Fehler, falls n < 0 oder nicht ganzzahlig
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <=1:
        return 1
    else:
        return n*fact_rec(n-1)
    
def fact_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(fact_rec(5))
print (fact_for(5))

t1=np.mean(timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100))
print("Average execution time for fact_rec: {}".format(t1))

t2=np.mean(timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100))
print("Average execution time for fact_for: {}".format(t2))

# fact_for ist um ein Faktor 11 schneller als fact_rec. Dies kommt daher, dass die rekursive Funktion mehrmals aufgerufen
# werden muss und der Wert mehrmals durch die if Abfragen durch muss, wobei er in der for Schleife einfach straight forward berechnet werden kann.

for n in range(190, 201):
    print("fact_rec({}) = {}".format(n,fact_rec(n)))
    print("fact_for({}) = {}".format(n,fact_for(n)))

# In Python gibt es keinen maximalen Integer. Die Obergrenze ist dynamisch, abhängig von dem ausführenden Gerät.


for n in range(170, 172):
    print("fact_rec({}) = {}".format(n,float(fact_rec(n))))
    print("fact_for({}) = {}".format(n,float(fact_for(n))))

# Folgender Fehler wird ausgegeben für die Fakultät von 171: int too large to convert to float
# Die größte darstellbare positive Gleitkommazahl in Python ist in der Regel etwa 1.8 × 10^308, und die kleinste darstellbare positive Gleitkommazahl
# ist etwa 5.0 × 10^-324. Wenn eine Gleitkommazahl einen größeren Wert erreicht, wird sie als "inf" (Unendlich) dargestellt, was auf einen Überlauf 
# hinweist. Wenn eine Gleitkommazahl kleiner als die kleinste darstellbare positive Zahl wird, wird sie als Null dargestellt.

