class User:
    def __init__(self, first_name, last_name, age, nationality, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.city = city
        self.full_name = first_name + last_name

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

ravikant = User("Ravikant", "Rajpoot", 21, "Indian", "Jhansi")
ravikant.describe_user()
ravikant.greet_user()
