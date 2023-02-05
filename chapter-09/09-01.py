class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        print(
            f"The Restaurant name is {self.name} and it's famous for its {self.cuisine} cuisine."
        )


restaurant = Restaurant("Jannaks", "North Indian")
restaurant.describe_restaurant()
