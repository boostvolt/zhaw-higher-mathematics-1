import numpy as np
import matplotlib.pyplot as plt

def s(max_value):
    n = 6
    x = []
    f = []
    s = 1 
    s = np.sqrt(2 - (2 * np.sqrt(1 - ((s ** 2)/4))))
    while n < max_value:
        x.append(n)
        f.append(s * 2 * n)
        s = np.sqrt(2 - (2 * np.sqrt(1 - ((s ** 2)/4))))
        n = 2 * n
    return (x,f)

x1, f1 = s(1000)  # Unpack the tuple

plt.plot(x1, f1, label='f1(x)')  # Plot the x and f1 values
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.ylim(6.2, 6.3)
plt.title('Polynomial')
plt.legend()
plt.grid()
plt.show()


# Für grosse n nähert sich der Wert immer mehr an 2 * pi. Dies kommt daher, 
# dass ein Kreis eigentlich auch nichts anderes ist als ein Vieleck mit sehr sehr vielen Ecken.


def s2(max_value):
    n = 6
    x = []
    f = []
    s = 1 
    s = np.sqrt((s ** 2) / (2 * (1 + (np.sqrt(1 - ((s ** 2)/4))))))
    while n < max_value:
        x.append(n)
        f.append(s * 2 * n)
        s = np.sqrt((s ** 2) / (2 * (1 + (np.sqrt(1 - ((s ** 2)/4))))))
        n = 2 * n
    return (x,f)

x1, f1 = s(1000)  # Unpack the tuple
x2, f2 = s2(1000)  # Unpack the tuple

print(f1,f2)


plt.plot(x1, f1, label='f1(x)')  # Plot the x and f1 values
plt.plot(x2, f2, label='f2(x)')  # Plot the x and f2 values
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.ylim(6.2, 6.3)
plt.title('Polynomial')
plt.legend()
plt.grid()
plt.show()

# Die beiden Kurven sind identisch und liegen im Plot direkt übereinander, weshalb nur eine Linie zu erkennen ist.