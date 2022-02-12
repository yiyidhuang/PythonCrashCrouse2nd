class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"The user is {self.last_name}.{self.first_name}")

    def greet_user(self):
        print(f"Hello, {self.last_name}.{self.first_name}")


jack = User('Jack', 'Welch')
bill = User('Bill', 'Gates')
newton = User('Isaac', 'Newton')

jack.describe_user()
jack.greet_user()

bill.describe_user()
bill.greet_user()

newton.describe_user()
newton.greet_user()
