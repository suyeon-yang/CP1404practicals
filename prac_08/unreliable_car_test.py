from prac_08.unreliable_car import UnreliableCar


def main():
    first_car = UnreliableCar("Ferrari", 100, 95)
    second_car = UnreliableCar("Lamborghini", 100, 20)

    for i in range(0, 5):
        print("{} drives {}km".format(first_car.name, first_car.drive(i)))
        print("{} drives {}km".format(second_car.name, second_car.drive(i)))

    print(first_car)
    print(second_car)


if __name__ == '__main__':
    main()
