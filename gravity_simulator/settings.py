class Settings:
    '''A class to store all settings for The Matrix'''

    def __init__(self):
        '''Initialize the gamne's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,5,0) # Deep green color.

        self.gravity = 9.8 / 60
        self.movement = 5