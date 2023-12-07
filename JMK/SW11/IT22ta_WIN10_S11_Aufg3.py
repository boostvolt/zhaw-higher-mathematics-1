# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 14:43:17 2020

Höhere Mathematik 1, Serie 11, Aufgabe 3 (Gerüst)

@author: knaa
"""
import numpy as np
import matplotlib.pyplot as plt

# number of pixels in x and y direction
detail = 1000
# maximum n for iterations (influences how detailed the structures are shown when zooming in)
maxit = 120


def calculate_mandelbrot(x_min, x_max, y_min, y_max, detail, maxit):
    # define real axis [x_min,x_max]
    a = np.linspace(x_min, x_max, detail, dtype=np.float64)
    # define imaginary axis [y_min,y_max]
    b = np.linspace(y_min, y_max, detail, dtype=np.float64)
    # for color values n
    B = np.zeros((detail, detail))

    # to create the complex plane with the axes defined by a and b
    [x, y] = np.meshgrid(a, b)
    # creating the plane
    C = np.array(x + y * 1j, np.complex128)
    # initial conditions (first iteration), Z has same dimension as C
    Z = np.zeros_like(C, np.complex128)

    # start iteration
    for n in np.arange(1, maxit + 1):
        # calculating Z
        Z = Z**2 + C
        # finding exploded values (i.e. with an absolute value > 2)
        expl = np.nonzero(np.abs(Z) > 2)
        # removing from iteration
        Z[expl] = 0
        # removing from plane
        C[expl] = 0
        # saving color value n
        B[expl] = n

    return B


# boundaries for the original image and the zoomed images
zooms = [(-2, 0.7, -1.4, 1.4), (-1.5, -1.3, -0.1, 0.1), (-0.8, -0.7, 0.1, 0.2)]

for i, (x_min_zoom, x_max_zoom, y_min_zoom, y_max_zoom) in enumerate(zooms):
    B = calculate_mandelbrot(
        x_min_zoom, x_max_zoom, y_min_zoom, y_max_zoom, detail, maxit
    )
    plt.figure(i + 1)
    plt.imshow(B, origin="lower", interpolation="bilinear")
    plt.show()
