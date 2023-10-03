import numpy as np
import matplotlib.pyplot as plt

eps = 1.0

while 1.0 + eps != 1.0:
    eps /= 2.0

print("Maschinengenauigkeit (eps) beträgt:", eps)
