import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color
        # self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # """Monitor the events of keyboard and mouse"""
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        sys.exit()
            self._check_events()

            if self.stats.game_active:
                # redraw the screen each time of the loops
                # self.screen.fill(self.settings.bg_color)
                # self.ship.blitme()

                self.ship.update()
                # self.bullets.update()
                self._update_bullets()

                # Delete the missing bullets
                # for bullet in self.bullets.copy():
                #    if bullet.rect.bottom <= 0:
                #        self.bullets.remove(bullet)
                # print(len(self.bullets))

                self._update_aliens()

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

        # Check if a bullet hit the alien. If so, delete the corresponding bullets and aliens
        # collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # if not self.aliens:
        #    # Delete all the bullets and create a new group of aliens
        #    self.bullets.empty()
        #    self._create_alien()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """In response to the collision between bullets and aliens"""
        # The collision between bullets and aliens occurred
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Update the location of all aliens in the alien crows"""
        self._check_fleet_edges()
        self.aliens.update()

        # Detect collisions between aliens and ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            # print("Ship hit!!!")
            self._ship_hit()
        # Check if any aliens have reached the bottom of the screen
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Deal with it like a ship was hit
                self._ship_hit()
                break

    def _ship_hit(self):
        """ship was hit by aliens"""
        if self.stats.ships_left > 0:
            # Subtract 1 from ships_left
            self.stats.ships_left -= 1

            # Clear the left aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new group aliens. Put the ship in the center at the bottom of the screen
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _create_fleet(self):
        """Create aliens groups"""
        # Create an alien and calculate how many aliens a row can hold
        # Create an alien
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Calculate how many lines the screen can hold
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Crete a group of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        # Create the first row aliens
        # for alien_number in range(number_aliens_x):
            # Create an alien and add it to the current line
            # alien = Alien(self)
            # alien.x = alien_width + 2 * alien_width * alien_number
            # alien.rect.x = alien.x
            # self.aliens.add(alien)
        #    self._create_alien(alien_number, row_number)
        # self.aliens.add(alien)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and add it to the current line"""
        alien = Alien(self)
        # alien_width = alien.rect.width
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """When aliens reach the edge, take corresponding measures"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move the whole group of aliens down and change their direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update the image on the screen and switch to a new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Create the game instance and run it.
    ai = AlienInvasion()
    ai.run_game()
