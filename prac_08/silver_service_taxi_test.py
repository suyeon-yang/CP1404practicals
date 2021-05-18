from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Silver Taxi", 100, 2)
    taxi.drive(18)
    print(taxi.calculate_fare())
    print(taxi)


if __name__ == '__main__':
    main()