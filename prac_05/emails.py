def main():
    email_to_name = {}
    email = input("What is your email?: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    """Extract expected name from given email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
