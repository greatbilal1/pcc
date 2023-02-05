class Restaurant:
    def __init__(
        self,
        name,
        cuisine,
    ):
        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"The Restaurant name is {self.name} and it's famous for its {self.cuisine} cuisine."
        )

    def increment_number_served(self, number):
        self.number_served += number

    def set_number_served(self, number):
        self.number_served = number


class IceCreamStand(Restaurant):
    def __init__(self):
        super().__init__("Jannaks", "North Indian")
        self.flavors = ["north", "south", "east", "west"]

    def describe_flavors(self):
        print("We have these flavors of ice-creams:")
        for flavor in self.flavors:
            print(f"- {flavor}")


icecream = IceCreamStand()
icecream.describe_flavors()
