class Meal:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_cost(self):
        return sum(item.price() for item in self.items)

    def show_items(self):
        for item in self.items:
            print(f"Item: {item.name()}, Price: {item.price()}")

# Products
class Burger:
    def name(self):
        return "Burger"

    def price(self):
        return 5.99

class Fries:
    def name(self):
        return "Fries"

    def price(self):
        return 2.99

class Drink:
    def name(self):
        return "Drink"

    def price(self):
        return 1.99

# Builder
class MealBuilder:
    def __init__(self):
        self.meal = Meal()

    def add_burger(self):
        self.meal.add_item(Burger())
        return self

    def add_fries(self):
        self.meal.add_item(Fries())
        return self

    def add_drink(self):
        self.meal.add_item(Drink())
        return self

    def build(self):
        return self.meal

# Client code
if __name__ == "__main__":
    meal_builder = MealBuilder()
    meal = meal_builder.add_burger().add_fries().add_drink().build()
    
    print("Your meal includes:")
    meal.show_items()
    print(f"Total cost: ${meal.get_cost():.2f}")
