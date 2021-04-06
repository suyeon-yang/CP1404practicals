MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit(choice)
            break
        elif choice == "F":
            fahrenheit_to_celsius(choice)
            break
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(choice):
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fahrenheit_to_celsius(choice):
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))


main()
