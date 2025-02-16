import sys

import pygame

from ship import Ship
from bullet import Bullet

def check_events(ss_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ss_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ss_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ss_settings, screen, ship, bullets)
        


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    

def update_screen(screen, ss_settings, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ss_settings.bg_color)
    # Redraw the ship at its current location.
    ship.blitme()
    # Draw the bullets at their current position.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def fire_bullet(ss_settings, screen, ship, bullets):
    """Fire a bullet."""
    new_bullet = Bullet(ss_settings, screen, ship)
    # Add the new bullet to bullets.
    bullets.add(new_bullet)

def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update the position of bullets.
    bullets.update()
    # Remove old bullets
    for bullet in bullets.copy():
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)