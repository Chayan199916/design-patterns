class House:
    def __init__(self):
        self.doors = 0
        self.windows = 0
        self.material = ""

    def __str__(self):
        return f"This is a {self.material} house with {self.doors} door(s) and {self.windows} window(s)."


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_doors(self, number):
        self.house.doors += number
        return self

    def add_windows(self, number):
        self.house.windows += number
        return self

    def set_material(self, material):
        self.house.material = material
        return self

    def build(self):
        return self.house


# Usage
builder = HouseBuilder()
my_house = (builder.set_material("Wood")
            .add_doors(2)
            .add_windows(4)
            .build())

print(my_house)
