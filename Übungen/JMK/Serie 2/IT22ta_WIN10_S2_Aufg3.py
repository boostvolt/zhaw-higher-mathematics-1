import matplotlib.pyplot as plt
import numpy as np

# Aufgabe 3


def s2n(n, subtask="a"):
    sn = 1

    repetitions = 0
    while n > 6:
        n /= 2
        repetitions += 1

    if n != 6:
        raise ValueError("n is not allowed")

    if subtask != "a" and subtask != "b":
        raise ValueError("subtask is not allowed")

    for _ in range(repetitions):
        if subtask == "a":
            sn = np.sqrt(2 - 2 * np.sqrt(1 - ((sn**2) / 4)))
        else:
            sn = np.sqrt(sn**2 / (2 * (1 + np.sqrt(1 - (sn**2 / 4)))))

    return sn


def generate_x_axis(i):
    generated_x_axis = np.zeros(i - 1)
    result = 3
    for count in range(0, i - 1):
        result *= 2
        generated_x_axis[count] = result

    return generated_x_axis.astype(int)


generate_x_axis = generate_x_axis(10)

## Aufgabe 3 a)
return_values = np.zeros(generate_x_axis.size)
for i in range(0, generate_x_axis.size):
    return_values[i] = 2 * generate_x_axis[i] * s2n(2 * generate_x_axis[i])

plt.figure()
plt.plot(generate_x_axis, return_values)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Aufgabe 3 a)")
plt.grid()
plt.show()

### Die Summe aller Seitenlänge nähert sich immer mehr an 2 * pi desto höher n gewählt wird, weil sich die Seiten immer mehr zu einem "Kreis" bilden.

## Aufgabe 3 b)
return_values = np.zeros(generate_x_axis.size)
for i in range(0, generate_x_axis.size):
    return_values[i] = 2 * generate_x_axis[i] * s2n(2 * generate_x_axis[i], "b")

plt.figure()
plt.plot(generate_x_axis, return_values)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Aufgabe 3 b)")
plt.grid()
plt.show()


### Es gibt keine Unterschiede, da es sich um eine mathematische Umformung handelt.
