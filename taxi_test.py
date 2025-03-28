from taxi import Taxi

def main():
    my_taxi = Taxi("Prius 1", 100)

    my_taxi.drive(40)
    print(f"{my_taxi}, current fare: ${my_taxi.get_fare():.2f}, remaining fuel: {my_taxi.fuel}")

    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}, current fare: ${my_taxi.get_fare():.2f},remaining fuel: {my_taxi.fuel}")

if __name__ == "__main__":
    main()