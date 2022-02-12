class Dog:
    """A simple attempt to simulate a dog"""

    def __init__(self, name, age):
        """Init the property, name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog squatting when ordered"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate a dog roll over when ordered"""
        print(f"{self.name} rolled over!")


# my_dog = Dog('Willie', 6)

# print(f"My dog's name is {my_dog.name}")
# print(f"My dog is {my_dog.age} years old")

# my_dog.sit()
# my_dog.roll_over()

# Multi Instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()
