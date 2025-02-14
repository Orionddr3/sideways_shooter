import sys
import pygame

from settings import Settings
import game_functions as gf

def run_game():
    """Initialize pygame, settings and a screen object."""
    pygame.init()
    ss_settings = Settings()
    screen = pygame.display.set_mode((ss_settings.screen_width, ss_settings.screen_height))
    pygame.display.set_caption("Sideways Shooter")

    # Main loop for the game
    while True:
        gf.check_events()

        screen.fill(ss_settings.bg_color)
        pygame.display.flip()

run_game()