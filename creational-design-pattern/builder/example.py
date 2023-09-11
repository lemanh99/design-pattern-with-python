from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.seats = []
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def add_seat(self, seat):
        self.seats.append(seat)


class Manual:
    def __init__(self):
        self.seats = []
        self.engine = None
        self.trip_computer = None
        self.gps = None

    def add_seat(self, seat):
        self.seats.append(seat)


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_seat(self, number):
        pass

    @abstractmethod
    def setengine(self, engine):
        pass

    @abstractmethod
    def settrip_computer(self, number_routes):
        pass

    @abstractmethod
    def setgps(self, x, y):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self._car = None
        self.reset()

    def reset(self):
        self._car = Car()

    def set_seat(self, number):
        self._car.add_seat(number)

    def setengine(self, engine):
        self._car.engine = engine

    def settrip_computer(self, number_routes):
        self._car.trip_computer = number_routes

    def setgps(self, x, y):
        self._car.gps = (x, y)

    def get_result(self) -> Car:
        return self._car


class ManualBuilder(Builder):
    def __init__(self):
        self._manual = None
        self.reset()

    def reset(self):
        self._manual = Manual()

    def set_seat(self, number):
        self._manual.add_seat(number)

    def setengine(self, engine):
        self._manual.engine = engine

    def settrip_computer(self, number_routes):
        self._manual.trip_computer = number_routes

    def setgps(self, x, y):
        self._manual.gps = (x, y)

    def get_result(self) -> Manual:
        return self._manual


class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def make_suv(self):
        self.builder.reset()
        self.builder.setengine("SUV")
        self.builder.set_seat(4)
        self.builder.settrip_computer(4)
        self.builder.setgps(10, 10)

    def make_sports_car(self):
        self.builder.reset()
        self.builder.setengine("SPORTS")
        self.builder.set_seat(2)
        self.builder.settrip_computer(2)
        self.builder.setgps(20, 20)

    def get_result(self):
        print(f"Builder engine: {self.builder.get_result().engine}")


if __name__ == "__main__":
    director = Director()
    car_builder = CarBuilder()
    director.builder = car_builder
    director.make_sports_car()
    director.get_result()
