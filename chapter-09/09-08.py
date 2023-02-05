class User:
    def __init__(self):
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.priviliges = ["can add post", "can delete user", "can ban user"]

    def show_privileges(self):
        print("Here are the priviliges for the admin:")
        for privilige in self.priviliges:
            print(f"- {privilige}")


class Admin(User):
    def __init__(self):
        super().__init__()
        self.privileges = Privileges()


alzywelzy = Admin()
alzywelzy.privileges.show_privileges()
