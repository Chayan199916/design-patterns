class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.wheels} wheels, and color {self.color}"


class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_engine(self, engine_type):
        self.car.engine = engine_type
        return self

    def set_wheels(self, wheels_count):
        self.car.wheels = wheels_count
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        return self.car


# Client code
if __name__ == "__main__":
    car_builder = CarBuilder()
    car = car_builder.set_engine("V8").set_wheels(4).set_color("Red").build()

    print(car)
