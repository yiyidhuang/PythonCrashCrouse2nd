class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'banana', 'milk']

    def show_flavors(self):
        for n in self.flavors:
            print("My flavors is " + n)


my_icecream = IceCreamStand('MXF', 'fastfood')
my_icecream.show_flavors()