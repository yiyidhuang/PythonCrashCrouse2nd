class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Make the game inactive at the beginning
        self.game_active = False

        self.high_score = 0


    def reset_stats(self):
        """Initialize statistics that may change during game operation"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
