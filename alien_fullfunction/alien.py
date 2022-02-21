import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a single alien"""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect property
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each alien was initially near the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the exact horizontal position of aliens
        self.x = float(self.rect.x)

    def check_edges(self):
        """If alien is at the edge of screen, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
