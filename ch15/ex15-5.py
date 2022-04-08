from random import choice


class RandomWalk:
    """A class that generates random walk data"""

    def __init__(self, num_points=5000):
        """Initialize random walk properties"""
        self.num_points = num_points

        # All walks begin with (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance of walking"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        return step

    def fill_walk(self):
        """Keep walking until the list reaches the specified length"""
        while len(self.x_values) < self.num_points:

            # Determine the direction and the distance in this direction
            x_step = self.get_step()
            y_step = self.get_step()

            # Refuse to stand still
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the X and Y values of the next point
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append()
            self.y_values.append()
