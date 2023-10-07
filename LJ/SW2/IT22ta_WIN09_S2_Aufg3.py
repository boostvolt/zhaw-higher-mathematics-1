import numpy as np
import matplotlib.pyplot as plt

# Wir beginnen beim Start Wert n = 6 und haben als maximalen Wert n = 1000 festgelegt, 
# da dies gross genug ist um die Annäherung an 2 * pi zu erkennen und bei noch grösseren 
# Zahlen keine deutliche Verbesserung bemerkbar ist.

def s(max_value):
    n = 6
    s = 1 
    x = []
    f = []
    x.append(n)
    f.append(s)
    s = np.sqrt(2 - (2 * np.sqrt(1 - ((s ** 2)/4))))
    while n < max_value:
        x.append(n)
        f.append(s * 2 * n)
        s = np.sqrt(2 - (2 * np.sqrt(1 - ((s ** 2)/4))))
        n = 2 * n
    return (x,f)

x1, f1 = s(1000)

plt.plot(x1, f1, label='f1(x)')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.ylim(6.2, 6.3)
plt.title('Polynomial')
plt.legend()
plt.grid()
plt.show()


# Für grosse n nähert sich der Wert immer mehr an 2 * pi. Dies kommt daher, 
# dass ein Kreis eigentlich auch nichts anderes ist, als ein Vieleck mit sehr sehr vielen Ecken.


def s2(max_value):
    n = 6
    s = 1 
    x = []
    f = []
    x.append(n)
    f.append(s)
    s = np.sqrt((s ** 2) / (2 * (1 + (np.sqrt(1 - ((s ** 2)/4))))))
    while n < max_value:
        x.append(n)
        f.append(s * 2 * n)
        s = np.sqrt((s ** 2) / (2 * (1 + (np.sqrt(1 - ((s ** 2)/4))))))
        n = 2 * n
    return (x,f)

x1, f1 = s(3000000000)
x2, f2 = s2(3000000000)

plt.plot(x1, f1, label='f1(x)')
plt.plot(x2, f2, label='f2(x)')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Polynomial')
plt.legend()
plt.grid()
plt.show()

# Der Graph von f1 wird zuerst immer genauer  bis er einen gewissen Wert erreicht, ab welchem die Aussage stark abweicht, bis sie dann auf 0 konvergiert.
# Der Graph von f2 hingegen konvergiert immer mehr näher gegen 2 * pi.