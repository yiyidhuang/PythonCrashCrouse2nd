from random import choice


class RandomWalk:
    """A class that generates random walk data"""

    def __init__(self, num_points=5000):
        """Initialize random walk properties"""
        self.num_points = num_points

        # All random walks begin with (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all points included in the random walk"""

        # Keep walking until the list reaches the specified length
        while len(self.x_values) < self.num_points:

            # Determine the direction and the distance in this direction
            x_direction = choice([1, -1])

            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Refuse to stand still
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the X and Y of the next point
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
