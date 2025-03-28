from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Main function to run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                choice = int(input("Choose taxi: "))
                if 0 <= choice < len(taxis):
                    current_taxi = taxis[choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input")
        elif menu_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance > 0:
                        current_taxi.start_fare()
                        distance_driven = current_taxi.drive(distance)
                        trip_cost = current_taxi.get_fare()
                        total_bill += trip_cost
                        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    else:
                        print("Distance must be positive")
                except ValueError:
                    print("Invalid input")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == '__main__':
    main()