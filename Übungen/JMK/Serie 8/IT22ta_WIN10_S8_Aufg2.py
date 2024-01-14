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

import timeit

import numpy as np


def Serie8_Aufg2(A):
    A = np.copy(A)  # necessary to prevent changes in the original matrix A_in
    A = A.astype("float64")  # change to float

    n = np.shape(A)[0]

    if n != np.shape(A)[1]:
        raise Exception("Matrix is not square")

    Q = np.eye(n)
    R = A

    for j in np.arange(0, n - 1):
        a = np.copy(R[j:, j]).reshape(n - j, 1)
        e = np.eye(np.size(a))[:, 0].reshape(n - j, 1)
        length_a = np.linalg.norm(a)
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * length_a * e
        u = (1 / np.linalg.norm(v)) * v
        H = np.eye(np.size(a)) - (2 * u.dot(u.T))
        Qi = np.eye(n)
        Qi[j:, j:] = H
        R = Qi.dot(R)
        Q = Q.dot(Qi.T)

    return (Q, R)


print(Serie8_Aufg2(np.array([[1, -2, 3], [-5, 4, 1], [2, -1, 3]])))


# Aufgabe 2c)
A = np.array([[1, -2, 3], [-5, 4, 1], [2, -1, 3]])

print(
    "Average execution time of Serie8_Aufg2: {} seconds".format(
        np.mean(
            timeit.repeat(
                "Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100
            )
        )
    )
)

print(
    "Average execution time of np.linalg.qr(A): {} seconds".format(
        np.mean(
            timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
        )
    )
)

## Average execution time of Serie8_Aufg2: 0.003652524994686246 seconds
## Average execution time of np.linalg.qr(A): 0.0007991502003278584 seconds


# Aufgabe 2d)
A = np.random.rand(100, 100)

print(
    "Average execution time of Serie8_Aufg2: {} seconds".format(
        np.mean(
            timeit.repeat(
                "Serie8_Aufg2(A)", "from __main__ import Serie8_Aufg2, A", number=100
            )
        )
    )
)

print(
    "Average execution time of np.linalg.qr(A): {} seconds".format(
        np.mean(
            timeit.repeat("np.linalg.qr(A)", "from __main__ import np, A", number=100)
        )
    )
)

## Average execution time of Serie8_Aufg2: 2.5209648332034704 seconds
## Average execution time of np.linalg.qr(A): 0.11862277499749325 seconds

## The difference in execution times between Serie8_Aufg2(A) and np.linalg.qr(A) is due to the efficiency of the algorithms used and the optimization done in the numpy library.
## np.linalg.qr(A) is a function from the numpy library, which is highly optimized for performance.
## It uses efficient algorithms and is implemented in C, which is faster than Python.
