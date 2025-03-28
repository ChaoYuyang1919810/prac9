from unreliable_car import UnreliableCar
import random


def main():
    # Seed the random number generator for reproducible results
    random.seed(12)

    # Test an UnreliableCar with 30% reliability
    unreliable_car = UnreliableCar("Old Clunker", 100, 30)
    print(f"Testing {unreliable_car.name} with {unreliable_car.reliability}% reliability:")
    successful_drives = 0
    total_distance = 0

    for i in range(100):
        distance = unreliable_car.drive(1)
        if distance > 0:
            successful_drives += 1
            total_distance += distance

    print(f"Successfully drove {successful_drives} times out of 100 attempts.")
    print(f"Total distance driven: {total_distance} km\n")

    # Test a car with 100% reliability
    reliable_car = UnreliableCar("Reliable Racer", 100, 100)
    print(f"Testing {reliable_car.name} with {reliable_car.reliability}% reliability:")
    distance = reliable_car.drive(50)
    print(f"Drove {distance} km (expected 50 if there's enough fuel)\n")

    # Test a car with 0% reliability
    no_go_car = UnreliableCar("No Go", 100, 0)
    print(f"Testing {no_go_car.name} with {no_go_car.reliability}% reliability:")
    distance = no_go_car.drive(10)
    print(f"Drove {distance} km (expected 0)")


if __name__ == '__main__':
    main()