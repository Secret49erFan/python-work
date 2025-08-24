import pygame

import random

from pygame.sprite import Sprite

class Droplet(Sprite):
    '''A class to generate a "Matrix" character'''
    def __init__(self, the_terminal):
        '''Initiate the character attributes'''
        super().__init__()
        # Create an instance of the Terminal class.
        self.terminal = the_terminal
        # Get a rectangle of the terminal screen to check boundries.
        self.screen_rect = self.terminal.screen.get_rect()
        # Set the font for the font object.
        self.font = pygame.font.Font('the_matrix\digital_rain\matrix_code_nfi.ttf', self.terminal.settings.char_font_size)
        # Get a random character and draw it to surface.
        self.char = self._get_random_char()
        self.image = self.font.render(self.char, True, self.terminal.settings.char_font_color)
        # Rectangle and finer control with a y-pos.
        self.rect = self.image.get_rect()
        # Get the height of the character.
        self.char_height = self.image.get_height()

    def update(self):
        '''Check for the droplet's position and update it'''
        self._rain()
        self._reset_to_top()
    
    def _rain(self):
        '''Simulate the droplets falling.'''
        # Droplets will fall by the amount set in rain_speed.
        self.rect.y += self.terminal.settings.rain_speed

    def _reset_to_top(self):
        '''Moves droplet back the top of screen after leaving bottom edge.'''
        if self.rect.top > self.terminal.rect.bottom:
            self.rect.bottom = 0
            
    def _get_random_char(self):
        '''Get a random character generated from a list comprehension.'''
        # List comprehension:
        # Get str text w/chr() passing var 'c' for each uniCode in range()
        # If uniCode retuned by ord() from '0' to 'z' is num or letter; save to list. 
        characters = [chr(c) for c in range(ord('0'), ord('z') + 1) if chr(c).isalnum()] # Only alphnumerica chars.
        # Pick a character in the generated list
        return random.choice(characters)
    
    def redraw_char(self):
        '''Redraw the charcter to the terminal screen.'''
        self.terminal.screen.blit(self.image, self.rect)