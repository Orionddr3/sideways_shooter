"""A module that contains the Bullet class"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ss_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, ss_settings.bullet_width, ss_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # Store the bullet's position as decimal value.
        self.x = float(self.rect.x)

        # Set the bullet's color and speed
        self.color = ss_settings.bullet_color
        self.speed_factor = ss_settings.bullet_speed_factor

        # Store the screen rect
        self.screen_rect = screen.get_rect()

    def update(self):
        """Move the bullet right."""
        # Update the decimal position of the bullet.
        self.x += self.speed_factor
        # Update the rect position.
        self.rect.x = self.x
    
    def draw_bullet(self):
        """Display the bullet at the current position."""
        pygame.draw.rect(self.screen, self.color, self.rect)