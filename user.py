# user_0 = {
#    'username': 'efermi',
#    'first': 'enrico',
#    'last': 'fermi',
#}

#for key, value in user_0.items():
#    print(f"\nKey: {key}")
#    print(f"Value: {value}")


class User:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.full_name = self.first_name.title() + ' ' + self.last_name.title()

    def describe_user(self):
        print("First name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Address: " + self.address.title())

    def greet_user(self):
        self.full_name = self.first_name.title() + ' ' + self.last_name.title()
        print("Welcome come to enjoy us, " + self.full_name.title() + "!")
