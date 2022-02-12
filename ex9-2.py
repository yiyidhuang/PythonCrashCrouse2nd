class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}, its cuisine type is {self.cuisine}")

    def open_restaurant(self):
        print("The restaurant is openning!")


KFC = Restaurant('KFC', 'noshery')
CUIHUA = Restaurant('CuiHua', 'Cantonese cuisine')
DAZHIMEN = Restaurant('Dazhaimen', 'Sichuan cuisine')

KFC.describe_restaurant()
CUIHUA.describe_restaurant()
DAZHIMEN.describe_restaurant()
