class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}, its cuisine type is {self.cuisine}")

    def open_restaurant(self):
        print("The restaurant is openning!")

    def set_number_served(self, served_number):
        self.number_served = served_number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('KFC', 'noshery')
print(f"There are {restaurant.number_served} customers in this restaurant")

restaurant.set_number_served(10)
print(f"There are {restaurant.number_served} customers in this restaurant")

restaurant.increment_number_served(50)
print(f"There are {restaurant.number_served} customers in this restaurant")
