from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness and flagfall."""
    flagfall = 4.50  # Class variable for the additional charge per fare

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the total fare including the flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation with the flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"