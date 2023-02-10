def convert_base(decimal_number):
    # binary
    binary = ''
    while decimal_number > 0:
        binary = str(decimal_number % 2) + binary
        decimal_number = decimal_number // 2

    # octal
    octal = ''
    decimal_number = int(binary, 2)
    while decimal_number > 0:
        octal = str(decimal_number % 8) + octal
        decimal_number = decimal_number // 8

    # hexadecimal
    hexadecimal = ''
    decimal_number = int(binary, 2)
    hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while decimal_number > 0:
        hex_digit = decimal_number % 16
        if hex_digit in hex_map:
            hexadecimal = hex_map[hex_digit] + hexadecimal
        else:
            hexadecimal = str(hex_digit) + hexadecimal
        decimal_number = decimal_number // 16

    return binary, octal, hexadecimal

decimal_number = int(input("Enter a decimal number: "))
binary, octal, hexadecimal = convert_base(decimal_number)
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
