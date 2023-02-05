class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        print(
            f"The Restaurant name is {self.name} and it's famous for its {self.cuisine} cuisine."
        )


jannaks = Restaurant("Jannaks", "North Indian")
jannaks.describe_restaurant()

jhansi_hotel = Restaurant("Jhansi Hotel", "South Indian")
jhansi_hotel.describe_restaurant()

joker_cafe = Restaurant("Joker Cafe", "North East Indian")
joker_cafe.describe_restaurant()
