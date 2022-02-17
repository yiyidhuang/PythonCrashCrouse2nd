class Settings:
    """Class that stores all settings in the game alien invasion"""

    def __init__(self):
        """Initialize the setting of the game"""
        # Set the screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Setup ship
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Setup bullet
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Setup alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction, 1 means to move to the right, and -1 means to the move to the left.
        self.fleet_direction = 1
