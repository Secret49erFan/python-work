import pygame

import random

from pygame.sprite import Sprite

from settings import Settings

class Droplet(Sprite):
    '''A class to draw a "Matrix" character'''
    def __init__(self, the_terminal):
        '''Initiate the character attributes'''
        super().__init__()
        self.screen = the_terminal.screen
        self.screen_rect = the_terminal.screen.get_rect()
        self.settings = the_terminal.settings
        # Set the font for the font object.
        self.font = pygame.font.Font('the_matrix/Matrix-Code.ttf', self.settings.char_font_size)
        # Get a random character and draw it to surface.
        self.char = self._get_random_char()
        self.char_surface = self.font.render(self.char, True, self.settings.char_font_color)
        # Rectangle and finer control with a y-pos.
        self.rect = self.char_surface.get_rect()
        self.y_pos = 0.0

    def update(self):
        self._rain()
    
    def _rain(self):
        pass
    
    def _get_random_char(self):
        characters = [chr(i) for i in range(ord('1'), ord('9') + 1)]
        return random.choice(characters)
    
    def _render_char(self, position):
        self.screen.blit(self.char_surface, position)

class Chain:
    '''A class to create a chain of characters'''
    def __init__(self):
        '''Initiate the chain attributes'''
        # This will be random after testing rendering.
        self.length_of_chain = 7
        self.droplets = pygame.sprite.Group()
        # This will be random after testing rendering.
        self.x_pos = 600
        # This will be above the screen after testing rendering.
        self.base_y_pos = 400