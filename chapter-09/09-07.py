class User:
    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.priviliges = ["can add post", "can delete user", "can ban user"]

    def show_privileges(self):
        print("Here are the priviliges for the admin {self.name}:")
        for privilige in self.priviliges:
            print(f"- {privilige}")


alzywelzy = Admin("alzywelzy")
alzywelzy.show_privileges()
