import pygame

from pygame.sprite import Sprite

class Ship(Sprite):
    """Class that manage ship"""
    def __init__(self, ai_game):
        super().__init__()
        """Initialize ship and set its intial position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and obtain its circumscribed rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # For each new ship, place it in the center at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the minimum value in the ship's attribute X
        self.x = float(self.rect.x)

        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Adjust the position of the ship according to the moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # According to self X update rect object
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at the specified location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Put the ship in the middle of the bottom of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
