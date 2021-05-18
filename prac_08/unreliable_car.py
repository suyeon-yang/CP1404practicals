import random
from prac_08.car import Car


class UnreliableCar(Car):
    """An unreliable Car object."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car based on reliability."""
        random_number = random.randint(0, 100)
        if random_number > self.reliability:
            distance = 0
        driven_meters = super().drive(distance)
        return driven_meters




