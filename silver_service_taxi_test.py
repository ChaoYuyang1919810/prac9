from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    # Test fare calculation with fanciness 2 and 18 km drive
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    expected_fare = (1.23 * 2 * 18) + 4.50  # 44.28 + 4.50 = 48.78 before rounding
    assert fare == expected_fare, f"Expected fare ${expected_fare:.2f}, got ${fare:.2f}"

def test_silver_service_taxi_after_rounding():
    # Test after modifying Taxi's get_fare to round to nearest 10 cents
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    fare = taxi.get_fare()
    expected_fare = 48.80  # After rounding in Taxi's get_fare
    assert fare == expected_fare, f"Expected fare ${expected_fare:.2f}, got ${fare:.2f}"

if __name__ == "__main__":
    test_silver_service_taxi()
    # test_silver_service_taxi_after_rounding()
    print("All tests passed.")