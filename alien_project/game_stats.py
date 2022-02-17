class GameStats:
    """Track game statistics"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # The game is active when it first start
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that may change during game operation"""
        self.ships_left = self.settings.ship_limit
