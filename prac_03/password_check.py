MIN_LENGTH = 5


def main():
    password = input("Enter password with at least {} characters: ".format(MIN_LENGTH))
    get_password(password)


def get_password(password):
    """Print asterisks upon length of password minimum of five characters."""
    while len(password) < MIN_LENGTH:
        print("Your password is too short")
        password = input("Enter password with at least {} characters: ".format(MIN_LENGTH))
    print('*' * len(password))


main()





