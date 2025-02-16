"""A module that contains the Bullet class"""

import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen, ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set the correct position.
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # Store the bullet's position as decimal value
        self.x = float(self.rect.x)

        # Set the bullet's color and speed
        self.color = (60, 60, 60)
        self.speed_factor = 1
