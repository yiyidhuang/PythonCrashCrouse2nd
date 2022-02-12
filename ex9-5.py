class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + self.last_name.title())

    def greet_user(self):
        print("Hello, " + self.first_name.title() + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts


einstein = User('Albert', 'Einstein')
einstein.describe_user()
for n in range(4):
    einstein.increment_login_attempts()
print(einstein.login_attempts)
einstein.reset_login_attempts()
print(einstein.login_attempts)
