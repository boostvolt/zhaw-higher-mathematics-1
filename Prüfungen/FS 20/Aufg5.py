# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:49:02 2020

SEP FS20 Aufgabe 5

@author: knaa
"""

"""
a) Gleichungssystem
A =

  240   120    80
   60   180   170
   60    90   500
    
b =

        3080
        4070
        5030

b) Gauss Schritte
i=1,j=2 =

        240         120          80        3080
           0         150         150        3300
          60          90         500        5030

i=1,j=3 =

         240         120          80        3080
           0         150         150        3300
           0          60         480        4260
           
i=2,j=3 =

         240         120          80        3080
           0         150         150        3300
           0           0         420        2940
Rückwärts einsetzen ergiebt: x1 = 3, x2=15, x3=7

c) Relativer und Absoluter Fehler
 || x - x~|| <= || A^-1 ||*||b-b~|| in inf norm == 0.0113*609 == 6.8875
 || x - x~|| / || x || <= ||A||*|| A^-1 ||*||b-b~||/||b|| in inf norm ==
 650 * 0.0113*609/5030 == 0.89 = 89%

d) cond(A) = ||A||*|| A^-1 || = 7.3512

"""
