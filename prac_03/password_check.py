
MIN_LENGTH = 5


def main():
    get_password()


def get_password():
    password = input("Enter password with at least {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Your password is too short")
        password = input("Enter password with at least {} characters: ".format(MIN_LENGTH))
    print('*' * len(password))


main()





