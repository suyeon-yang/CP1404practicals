from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def calculate_fare(self):
        return (self.price_per_km * self.current_fare_distance) + self.flag_fall

    def __str__(self):
        return "{}, plus flagfall of ${}".format(super().__str__(), self.flag_fall)