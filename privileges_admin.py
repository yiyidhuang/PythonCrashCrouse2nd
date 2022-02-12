from user import User


class Admin(User):
    def __init__(self, first_name, last_name, address):
        super().__init__(first_name, last_name, address)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for n in self.privileges:
            print("This admin " + n)
