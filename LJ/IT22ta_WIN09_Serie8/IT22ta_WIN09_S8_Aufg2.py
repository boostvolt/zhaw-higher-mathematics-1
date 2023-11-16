# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020
 
Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2
 
Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix            
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]])
        [Q,R]=Serie8_Aufg2(A)
 
@author: knaa
"""
import numpy as np
from IT22ta_WIN09_S6_Aufg2 import obereDreiecksMatrix
import timeit

# Aufgabe 2a)
def Serie8_Aufg2(A):
   
   
   
    A = np.copy(A)                       #necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')              #change to float
   
    n = np.shape(A)[0]
   
    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square')
   
    Q = np.eye(n)
    R = A
   
    for j in np.arange(0,n-1):
        a = np.copy(R[j:,j]).reshape(n-j,1)  
        e = np.eye(n-j)[0,:].reshape(n-j,1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0: sig = 1
        else: sig = -1
        v = a + (sig * length_a * e)
        u = (1 / np.linalg.norm(v))* v
        H = np.eye(n-j)- (2 * np.dot(u,np.transpose(u)))
        Qi = np.eye(n)
        Qi[j:,j:] = H
        R = np.dot(Qi,R)
        Q = np.dot(Q,np.transpose(Qi))
       
    return(Q,R)

#Aufgabe 2b) 
A = np.array([[1,-2,3], [-5,4,1], [2,-1,3]])
[Q, R] = Serie8_Aufg2(A)
b = np.array([1,9,5])
bneu = np.dot(b,Q)

print("Die Lösung für Q lautet {} und die Lösung für R lautet {}".format(Q,R))
#[x1, x2, x3] = np.linalg.solve(R, bneu)
#print("Die Lösung für Aufgabe 1 lautet x1 = {}, x2 = {} und x3 = {}.".format(x1, x2, x3))
print("Die Lösung für Aufgabe 1 lautet x = {}.".format(np.linalg.solve(R, bneu)))

#Aufgabe 2c)
t1=timeit.repeat("Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100) 
t2=timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
avg_t1 = np.average(t1)/100
avg_t2 = np.average(t2)/100
print("Die Laufzeit1 unserer eigenen Funktion beträgt: {} und die Laufzeit von linalg.qr() beträgt {} für eine 3x3 Matrix".format(avg_t1, avg_t2))
print("Unsere Funktion ist {} mal langsamer für eine 3x3 Matrix".format(avg_t1/avg_t2))

#Aufgabe 2d)
Test = np.random.rand(100,100)
t3=timeit.repeat("Serie8_Aufg2(Test)", "from __main__ import Serie8_Aufg2, Test", number=100) 
t4=timeit.repeat("np.linalg.qr(Test)", "from __main__ import np, Test", number=100)
avg_t3 = np.average(t3)/100
avg_t4 = np.average(t4)/100
print("Die Laufzeit unserer eigenen Funktion beträgt: {} und die Laufzeit von linalg.qr() beträgt {} für eine 100x100 Matrix".format(avg_t3, avg_t4))
print("Unsere Funktion ist {} mal langsamer bei der Berechnung einer 100x100 Matrix".format(avg_t3/avg_t4))
print("Unsere Funktion wird von einer 3x3-Matrix zu einer 100x100-Matrix um den Faktor {} langsamer.".format(avg_t3/avg_t1))
print("Die interne Funktion von Python wird nur {} mal langsamer".format(avg_t4/avg_t2))

#Die Laufzeit1 unserer eigenen Funktion beträgt: 2.472667198162526e-05 und die Laufzeit von linalg.qr() beträgt 9.948334016371518e-06 für eine 3x3 Matrix
#Unsere Funktion ist 2.485508823983363 mal langsamer für eine 3x3 Matrix
#Die Laufzeit unserer eigenen Funktion beträgt: 0.025264274747984018 und die Laufzeit von linalg.qr() beträgt 0.0007007724979193881 für eine 100x100 Matrix
#Unsere Funktion ist 36.052035179739946 mal langsamer bei der Berechnung einer 100x100 Matrix
#Unsere Funktion wird von einer 3x3-Matrix zu einer 100x100-Matrix um den Faktor 1021.7418165597967 langsamer.
#Die interne Funktion von Python wird nur 70.4411911347326 mal langsamer