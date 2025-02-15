import sys

import pygame

import ship

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ship.moving_down = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                ship.moving_down = False
            if event.key == pygame.K_UP:
                ship.moving_up = False


def update_screen(screen, ss_settings, ship):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ss_settings.bg_color)
    # Redraw the ship at its current location.
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()