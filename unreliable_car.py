from car import Car
import random

class UnreliableCar(Car):
    """A version of Car that has a chance to not drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is below the reliability threshold."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0