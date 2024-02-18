# Name: Danny Cortes
# Name of the program: Binary Conversion Calcuator
# Purpose: Create a calculator to convert binary to decimal or decimal to binary

def intro_msg():
    print("Im going to create a program that can convert a decimal number to binary and a binary number to decimal.")

def binary_to_decimal(number):
        result = 0
        if len(number) > 0:
            power = len(str(number)) -1 # Determines greatest power
            for num in str(number):
                result += int(num) + 2 ** power
                power -= 1 # decrease by 1
            return result

def decimal_to_binary(number):
    result = ""
    number = int(number)
    while number > 0: # Keep dividing at 0
        remainder = number % 2 # % in python means the remainder
        number = number // 2
        result = str(number) + result #place the string in reverse
    return result

# MAIN MENU FUNCTION

def menu():
    ACTIONS = {
        '1': ("Binary Number (8-digits)", binary_to_decimal),
        '2': ("Decimal Number (0-255)", lambda x: decimal_to_binary(int(x))),
    }

    while True:
        print("\n*** Binary Calculator ***\n" + "-" * 42)
        print("(1) Binary to Decimal Conversion")
        print("(2) Decimal to Binary Conversion")
        print("(q) Quit")

        choice = input(">> ").lower()

        if choice == 'q':
            print("\nGoodbye!")
            break
        elif choice in ACTIONS:
            inputs = [input(f"\nEnter {prompt} : ") for prompt in ACTIONS[choice][:-1]]
            print("=", ACTIONS[choice][-1](*inputs))
        else:
            print("\nMake a valid selection!")

def main():
    intro_msg()
    menu()

if __name__ == "__main__":
    main()
