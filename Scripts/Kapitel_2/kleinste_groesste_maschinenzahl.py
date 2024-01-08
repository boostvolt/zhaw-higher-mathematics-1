def get_l_min(basis_exponent, exponent_stellen, debug=False):
    groesste_zahl_im_system = basis_exponent - 1
    smallest_binary_number = "-" + f"{groesste_zahl_im_system}" * (exponent_stellen)
    if debug:
        print(
            f"Kleinste Zahl im {basis_exponent}-System mit {exponent_stellen} Stellen: 0.1 * {basis_exponent}^{smallest_binary_number}"
        )
    decimal_value = int(smallest_binary_number, basis_exponent)
    return decimal_value


def get_l_max(basis_exponent, exponent_stellen, debug=False):
    groesste_zahl_im_system = basis_exponent - 1
    smallest_binary_number = f"{groesste_zahl_im_system}" * (exponent_stellen)
    if debug:
        print(
            f"Groesste Zahl im {basis_exponent}-System mit {exponent_stellen} Stellen: {basis_exponent}^{smallest_binary_number}"
        )
    decimal_value = int(smallest_binary_number, basis_exponent)
    return decimal_value


def kleinste_positive_maschinenzahl(
    basis, basis_exponent, exponent_stellen, debug=False
):
    l_min = get_l_min(basis_exponent, exponent_stellen, debug)
    if debug:
        print(f"B^(l_min - 1): {basis}^({l_min} - {1}) = {basis}^({l_min - 1})")
        print(f"Kleinste positive Maschinenzahl: {basis ** (l_min - 1)}")
    return basis**l_min - 1


def groesste_positive_maschinenzahl(
    basis, basis_exponent, mantisse_stellen, exponent_stellen, debug=False
):
    l_max = get_l_max(basis_exponent, exponent_stellen, debug)
    if debug:
        print(
            f"B^l_max - B^(l_max - n): {basis}^{l_max} - {basis}^({l_max} - {mantisse_stellen}) = {basis}^{l_max} - {basis}^{l_max - mantisse_stellen}"
        )
        print(
            f"Groesste positive Maschinenzahl: {(basis ** l_max) - (basis ** (l_max - mantisse_stellen))}"
        )
    return (basis**l_max) - (basis ** (l_max - mantisse_stellen))


# Achtung: Diese Funktion funktioniert für Dualsysteme für Basis und Exponent.
# Für alle anderen Systeme ist es nicht garantiert, dass die Lösung stimmt, weil wir keine Aufgaben hatten mit der wir es überprüfen konnten.

mantisse_stellen = 20
exponent_stellen = 4
basis = 2
basis_exponent = 2

kleinste_positive_maschinenzahl(basis, basis_exponent, exponent_stellen, True)
groesste_positive_maschinenzahl(
    basis, basis_exponent, mantisse_stellen, exponent_stellen, True
)
