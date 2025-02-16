"""A module that contains the settings class"""

class Settings():
    """A class to store all settings for Sideways Shooter"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.speed_factor = 1.5

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60,60, 60
        self.bullet_speed_factor = 1
