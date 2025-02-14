import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen, ss_settings):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ss_settings.bg_color)

    # Make the most recently drawn screen visible.
    pygame.display.flip()