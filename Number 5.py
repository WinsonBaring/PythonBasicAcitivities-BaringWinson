def decToBinary(dec):
    if dec == 0:
        return 0
    toBinary = ""
    while dec > 0:
        rem = dec % 2
        toBinary = str(rem) + toBinary
        dec = dec // 2
    return toBinary

def binaryToN(bin, type):
    if bin == 0:
        return "0"
    toDecimal = 0

    base = 1
    while bin > 0:
        rem = bin % 10
        toDecimal = toDecimal + rem * base
        base = base * 2
        bin = bin // 10

    if type == "D":
        return toDecimal

    elif type == "O":
        octal = ""
        while toDecimal > 0:
            rem = toDecimal % 8
            octal = str(rem) + octal
            toDecimal = toDecimal // 8
        return octal

    else:
        hexadecimal = ""
        while toDecimal > 0:
            rem = toDecimal % 16
            if rem < 10:
                hexadecimal = str(rem) + hexadecimal
            else:
                hexadecimal = chr(ord('A') + rem - 10) + hexadecimal
            toDecimal = toDecimal // 16
        return hexadecimal

def decToOctal(dec):
    if dec == 0:
        return 0
    toOctal = ""
    while dec > 0:
        rem = dec % 8
        toOctal = str(rem) + toOctal
        dec = dec // 8
    return toOctal

def decToHex(dec):
    if dec == 0:
        return "0"
    toHex = ""
    hex_digits = "0123456789ABCDEF"  # Define the hexadecimal digits

    while dec > 0:
        remainder = dec % 16
        toHex = hex_digits[remainder] + toHex
        dec = dec // 16

    return toHex


def main():
    while True:
        print("Choose an option:")
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("4. Binary to Decimal, Octal, or Hexadecimal")
        print("5. Exit")
        choice = int(input("Enter your choice (1/2/3/4/5): "))

        if choice == 1:
            decimal = int(input("Enter a decimal number: "))
            binary = decToBinary(decimal)
            print("Binary equivalent: ", binary)

        elif choice == 2:
            decimal = int(input("Enter a decimal number: "))
            octal = decToOctal(decimal)
            print("Octal equivalent: ", octal)

        elif choice == 3:
            decimal = int(input("Enter a decimal number: "))
            hexadecimal = decToHex(decimal)
            print("Hexadecimal equivalent: ", hexadecimal)

        elif choice == 4:
            bin = int(input("Enter a binary number: "))
            type = input("Choose conversion type (D/O/H): ").upper()
            result = binaryToN(bin, type)
            print(f"{type} equivalent: {result}")

        elif choice == 5:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

main()

