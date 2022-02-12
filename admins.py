class User:
    def __init__(self, first_name, last_name, username, email, location):
        """Initialize"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempt = 0

    def describe_user(self):
        print("\n" + self.first_name + " " + self.last_name)
        print("    Username: " + self.username)
        print("    Email: " + self.email)
        print("    Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)

        self.privileges = Privileges()


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)


