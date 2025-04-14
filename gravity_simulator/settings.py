class Settings:
    '''A class to store all settings for The Matrix'''

    def __init__(self):
        '''Initialize the gamne's settings.'''
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,5,0) # Deep green color.
        self.fps = 60

        self.gravity = 0
        self.movement = 7

        # Main circle settings
        self.cir_color = (250,250,250)
        self.cir_radius = 7

        # Grid circle settings
        self.grid_cir_color = (0,190,19)
        self.grid_cir_radius = 4
        self.grid_padding = 7