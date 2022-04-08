from random import randint


class Die:
    """Class representing a die"""

    def __init__(self, num_sides=6):
        """There are 6 sides one in a die."""
        self.num_sides = num_sides

    def roll(self):
        """Returns a random value between 1 and the number of dice faces"""
        return randint(1, self.num_sides)
