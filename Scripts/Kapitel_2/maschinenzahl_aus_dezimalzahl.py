def machine_number(value, exponent=8, mantissa=23):
    # Vorzeichen berechnen
    if value > 0:
        sign = "0"
    else:
        sign = "1"

    # Bias berechnen
    bias = 2 ** (exponent - 1) - 1

    # Vorkommastellen berechnen
    integerValue = abs(int(value))
    binaryIntegerValue = bin(integerValue)[2:]

    # Exponent berechnen
    binaryIntegerValueExponent = len(binaryIntegerValue) - 1

    # Nachkommastellen berechnen
    fractionalValue = abs(value) - abs(integerValue)
    binaryFractionalValue = convert_fraction_to_binary(fractionalValue)

    # Mantisse berechnen
    mantissaValue = binaryIntegerValue[1:] + binaryFractionalValue
    correctMantissaLength = mantissaValue[:mantissa]
    if len(correctMantissaLength) < mantissa:
        correctMantissaLength = correctMantissaLength + "0" * (
            mantissa - len(correctMantissaLength)
        )

    # bias berechnen
    biasValue = bin(binaryIntegerValueExponent + bias)[2:]

    # Ergebnis als String zusammenfassen
    strResult = str(
        "Vorzeichen (0 Positiv, 1 Negative): "
        + sign
        + "\n"
        + "Exponent: "
        + biasValue
        + "\n"
        + "Mantisse inklusive führende 1: 1."
        + correctMantissaLength
        + "\n"
        + "|"
        + sign
        + "|"
        + biasValue
        + "|"
        + correctMantissaLength
        + "|"
    )

    # Ergebnis
    return sign, biasValue, correctMantissaLength, strResult


def convert_fraction_to_binary(fraction):
    """Convert the fractional part of a decimal number to binary."""
    binary = ""
    while fraction and len(binary) < 64:  # Limit to 64 iterations
        fraction *= 2
        if fraction >= 1:
            binary += "1"
            fraction -= 1
        else:
            binary += "0"
    return binary


if __name__ == "__main__":
    result_machine_number = machine_number(value=3.5)
    print(result_machine_number[3])
