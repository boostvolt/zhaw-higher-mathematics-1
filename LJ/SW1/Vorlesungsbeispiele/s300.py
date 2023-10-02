def round_to_machine_number(x, n):
    if n == 3:
        precision = 1e-3
    elif n == 5:
        precision = 1e-5
    else:
        raise ValueError("Unsupported precision. Choose n = 3 or n = 5.")

    rounded_x = round(x / precision) * precision
    return rounded_x


def calculate_s300(ascending, n):
    s = 0.0
    if ascending:
        start = 1
        end = 301
        step = 1
    else:
        start = 300
        end = 0
        step = -1

    for i in range(start, end, step):
        term = 1 / (i**2)
        rounded_term = round_to_machine_number(term, n)
        s += rounded_term

    return round_to_machine_number(s,n)

# Berechnen Sie s300 aufsteigend mit 3-stelliger Genauigkeit
s300_ascending_3digits = calculate_s300(True, 3)

# Berechnen Sie s300 absteigend mit 3-stelliger Genauigkeit
s300_descending_3digits = calculate_s300(False, 3)

# Berechnen Sie s300 aufsteigend mit 5-stelliger Genauigkeit
s300_ascending_5digits = calculate_s300(True, 5)

# Berechnen Sie s300 absteigend mit 5-stelliger Genauigkeit
s300_descending_5digits = calculate_s300(False, 5)

print("s300 aufsteigend mit 3-stelliger Genauigkeit:", s300_ascending_3digits)
print("s300 absteigend mit 3-stelliger Genauigkeit:", s300_descending_3digits)
print("s300 aufsteigend mit 5-stelliger Genauigkeit:", s300_ascending_5digits)
print("s300 absteigend mit 5-stelliger Genauigkeit:", s300_descending_5digits)
