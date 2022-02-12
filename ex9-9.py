class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.read = 0

    def describle(self):
        long_name = str(self.year) + " " + self.make + " " + self.model + " "
        return long_name.title()

    def read(self):
        print("Miles: " + str(self.read) + ".")

    def update_read(self, x):
        if x < self.read:
            print("Invalid!")
        else:
            self.read = x

    def increase_read(self, x):
        if x < 0:
            print("Invalid!")
        else:
            self.read += x

    def fill_gas_tank(self):
        print("Test")


class Battery:
    def __init__(self, battery_size=70):
        self.batter_size = battery_size

    def describe_battery(self):
        print("Battery: " + str(self.batter_size))

    def get_range(self):
        if self.batter_size == 70:
            range = 240
        elif self.batter_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.batter_size != '85':
            self.batter_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year) # 继承Car类
        self.battery = Battery()

    def describle_battery(self):
        print("Battery: " + str(self.battery_size))

    def fill_gas_tank(self):
        print("The car does not have a tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.describle())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()



