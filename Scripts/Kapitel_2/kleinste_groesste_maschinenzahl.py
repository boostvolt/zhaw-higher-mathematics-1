def l_min(number_of_digits, debug=False):
    smallest_binary_number = "-" + "1" * (number_of_digits)
    if debug:
        print(
            f"Kleinste Zahl im Dualsystem mit {number_of_digits} Stellen: 0.1 * 2^{smallest_binary_number}"
        )
    decimal_value = int(smallest_binary_number, 2)
    return decimal_value


def l_max(number_of_digits, debug=False):
    smallest_binary_number = "1" * (number_of_digits)
    if debug:
        print(
            f"Groesste Zahl im Dualsystem mit {number_of_digits} Stellen: 2^{smallest_binary_number}"
        )
    decimal_value = int(smallest_binary_number, 2)
    return decimal_value


def kleinste_positive_maschinenzahl(basis, exponent_stellen, debug=False):
    if debug:
        print(
            f"B^(l_min - 1): {basis}^({l_min(exponent_stellen, debug)} - {1}) = {basis}^({l_min(exponent_stellen) - 1})"
        )
        print(
            f"Kleinste positive Maschinenzahl: {basis ** (l_min(exponent_stellen) - 1)}"
        )
    return basis ** (l_min(exponent_stellen) - 1)


def groesste_positive_maschinenzahl(
    basis, mantisse_stellen, exponent_stellen, debug=False
):
    if debug:
        print(
            f"B^l_max - B^(l_max - n): {basis}^{l_max(exponent_stellen, debug)} - {basis}^{l_max(exponent_stellen)} - {mantisse_stellen}) = {basis}^{l_max(exponent_stellen)} - {basis}^{l_max(exponent_stellen) - mantisse_stellen})"
        )
        print(
            f"Groesste positive Maschinenzahl: {basis ** l_max(exponent_stellen) - (basis ** (l_max(exponent_stellen) - mantisse_stellen))}"
        )
    return basis ** l_max(exponent_stellen) - (
        basis ** (l_max(exponent_stellen) - mantisse_stellen)
    )


# Achtung: Geht momentan nur im Dualsystem, weil wir keine andere Beispiele / Aufgaben
# hatten die mit einer anderen Basis oder anderen Exponenten-Basis gerechnet wurden

mantisse_stellen = 2
exponent_stellen = 1
basis = 2

kleinste_positive_maschinenzahl(basis, exponent_stellen, True)
groesste_positive_maschinenzahl(basis, mantisse_stellen, exponent_stellen, True)
