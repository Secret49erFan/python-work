class Settings:
    '''A class to store all settings for the terminal.'''

    def __init__(self):
        '''Initialize the gamne's settings.'''
         # Terminal settings.
        self.terminal_screen_size = (1200,800)
        self.fps = 60
        
        # Droplet settings.
        self.char_font_size = 28
        self.char_font_color = (0, 255, 0)
        self.rain_speed = 3.43

        # Chain settings.
        self.num_of_chains = 66
        self.min_chain_length = 17
        self.max_chain_length = 35
        self.max_chain_height = 2000
