import numpy as np
import matplotlib.pyplot as plt



detail = 1000                       #number of pixels in x and y direction
maxit = 120                         #maximum n for iterations (influences how detailed the structures are shown when zooming in)
x_min = -2                   #minimim value of x-interval
x_max = 0.7                   #maximum value of x-interval
y_min = -1.4                  #minimim vale of y-interval
y_max = 1.4                    #minimim vale of y-interval

a = np.linspace(x_min, x_max,detail,dtype=np.float64)  #define real axis [x_min,x_max]
b = np.linspace(y_min, y_max,detail,dtype=np.float64)  #define imaginary axis [y_min,y_max]

B = np.zeros((detail,detail))        #for color values n 

[x,y] = np.meshgrid(a,b)       #to create the complex plane with the axes defined by a and b
C = np.array(x+y*1j, np.complex128)     #creating the plane
Z = np.zeros_like(C, np.complex128)  #initial conditions (first iteration), Z has same dimension as C
for n in np.arange(1,maxit+1):       #start iteration
    Z = Z**2 + C                      #calculating Z
    expl = np.where(np.abs(Z) > 2)         #finding exploded values (i.e. with an absolute value > 2)
    Z[expl] = 0                        #removing from iteration
    C[expl] = 0                        #removing from plane
    B[expl] = n                #saving color value n

plt.figure(1)
B = B/np.max(np.max(B))           #deviding by max value for correct color
plt.imshow(B,extent=[x_min,x_max,y_min,y_max],origin='lower',interpolation='bilinear')   #display image
plt.show()
zoom_regions = [(-1.5, -1.2, -0.2, 0.2), (-1.0, -0.8, -0.4, -0.2), (-0.75, -0.7, -0.2, -0.1)] 
for i, (new_x_min, new_x_max, new_y_min, new_y_max) in enumerate(zoom_regions):     
    plt.figure(i + 2)     
    a_zoom = np.linspace(new_x_min, new_x_max, detail, dtype=np.float64)     
    b_zoom = np.linspace(new_y_min, new_y_max, detail, dtype=np.float64)     
    [x_zoom, y_zoom] = np.meshgrid(a_zoom, b_zoom)     
    C_zoom = np.array(x_zoom + y_zoom*1j, np.complex128)     
    Z_zoom = np.zeros_like(C_zoom, np.complex128)     
    B_zoom = np.zeros((detail, detail))     
    for n in np.arange(1, maxit + 1):         
        Z_zoom = Z_zoom**2 + C_zoom         
        expl_zoom = np.where(np.abs(Z_zoom) > 2)         
        Z_zoom[expl_zoom] = 0        
        C_zoom[expl_zoom] = 0        
        B_zoom[expl_zoom] = n     
        B_zoom = B_zoom/np.max(np.max(B_zoom))     
    plt.imshow(B_zoom, extent=[new_x_min, new_x_max, new_y_min, new_y_max], origin='lower', interpolation='bilinear')     
    plt.title(f"Zoomed Mandelbrot Set {i + 1}")     
    plt.show()