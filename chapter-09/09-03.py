class User:
    def __init__(self, first_name, last_name, age, nationality, city, middle_name=""):
        self.first_name = first_name + " "
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.city = city

        if middle_name:
            self.middle_name = middle_name + " "
            self.full_name = self.first_name + self.middle_name + self.last_name
        else:
            self.full_name = self.first_name + self.last_name

    def describe_user(self):
        print(
            f"The user name is {self.full_name} and his name is {self.age}, {self.full_name} is from {self.city} and his nationality is {self.nationality}."
        )

    def greet_user(self):
        print(f"Hi there, {self.full_name}.")


manvendra = User("Manvendra", "Rajpoot", 21, "Indian", "Jhansi")
manvendra.describe_user()
manvendra.greet_user()

amit = User("Amit", "Rajpoot", 21, "Indian", "Jhansi")
amit.describe_user()
amit.greet_user()

ravikant = User("Ravikant", "Rajpoot", 21, "Indian", "Jhansi","Singh")
ravikant.describe_user()
ravikant.greet_user()

kamala = User("Kamala", "Rajpoot", 21, "Indian", "Jhansi", "Devi")
kamala.describe_user()
kamala.greet_user()
