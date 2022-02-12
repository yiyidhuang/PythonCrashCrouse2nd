class Car:
    """A simple attempt to simulate a car"""

    def __init__(self, make, model, year):
        """Init the property of the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return neat descriptive information"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a message indicating the car mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    # def update_odometer(self, mileage):
    #    """Set the odometer reading to the specified value"""
    #    self.odometer_reading = mileage
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the specified value
        Forbidden to callback the odometer reading
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increase the odometer reading by the specified amount"""
        self.odometer_reading += miles


# class Battery:
#    """A simple attempt to simulate a battery of electric car"""

#    def __init__(self, battery_size=75):
#        """Initialize the properties of a battery"""
#        self.battery_size = battery_size

#    def describe_battery(self):
#        """Print a message about the battery capacity"""
#        print(f"This car has a {self.battery_size}-kWh battery.")

#    def get_range(self):
#        """Print a message describing the range of battery"""
#        if self.battery_size == 75:
#            range = 260
#        elif self.battery_size == 100:
#            range = 315

#        print(f"This car can go about {range} miles on a full charge.")


# class ElectricCar(Car):
#    """To simulate the uniqueness of electric vehicles"""

#    def __init__(self, make, model, year):
#        """Initialize the properties of superclass, then initialize the special property of the electric car"""
#        super().__init__(make, model, year)
#        self.battery = Battery()

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())

# my_new_car.read_odometer()

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()


# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
