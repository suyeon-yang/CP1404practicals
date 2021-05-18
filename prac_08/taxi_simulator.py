from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU_CHOICE = ["q", "c", "d"]


def main():
    menu = "Let's drive!\nq)uit, c)hoose taxi, d)rive"
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print(menu)
    menu_choice = ""
    while menu_choice != "q":
        menu_choice = input(">>> ").lower()
        if menu_choice == "c":
            print("Taxis available:")
            print_taxi(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name,
                                                             trip_cost))
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    print_taxi(taxis)


def print_taxi(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()