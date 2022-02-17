import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # """Monitor the events of keyboard and mouse"""
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        sys.exit()
            self._check_events()

            # redraw the screen each time of the loops
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()

            self.ship.update()
            # self.bullets.update()
            self._update_bullets()

            # Delete the missing bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            # Make recently drawn screens visible
            # pygame.display.flip()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RIGHT:
                    # Move the ship to the right
                    # self.ship.rect.x += 1
                #    self.ship.moving_right = True
                # elif event.key == pygame.K_LEFT:
                #    self.ship.moving_left = True
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # if event.key == pygame.K_RIGHT:
                #    self.ship.moving_right = False
                # elif event.key == pygame.K_LEFT:
                #    self.ship.moving_left = False
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a bullet and add it to the group bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the location of bullets and delete missing bullets"""
        # Update the position of bullets
        self.bullets.update()

        # Delete the missing bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update the image on the screen and switch to a new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()


if __name__ == '__main__':
    # Create the game instance and run it.
    ai = AlienInvasion()
    ai.run_game()
