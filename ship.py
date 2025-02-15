"""This module contains the Ship class."""
import pygame

class Ship():
    """Models the ship in the game."""

    def __init__(self, ss_settings, screen):
        """Initializes the ship and sets its starting position."""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Rotate the ship 90 degrees to the right.
        self.image = pygame.transform.rotate(self.image, 270)

        # Place the ship at the left center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.y = self.rect.centery

        self.speed_factor = ss_settings.speed_factor

        # Movement flags
        self.moving_down = False
        self.moving_up = False
    
    def update(self):
        """Update the ship's position based on the movement flags."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed_factor
        
        self.rect.centery = self.y


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
