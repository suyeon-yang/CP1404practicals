from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other_guitar = Guitar("Another Guitar", 2012, 1512.9)

print("{} get_age() - Expected {}. Got {}".format(guitar.name, 99,
                                                  guitar.get_age()))
print("{} get_age() - Expected {}. Got {}".format(other_guitar.name, 9,
                                                  other_guitar.get_age()))
print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                     True,
                                                     guitar.is_vintage()))
print("{} is_vintage() - Expected {}. Got {}".format(other_guitar.name,
                                                     False,
                                                     other_guitar.is_vintage()))
