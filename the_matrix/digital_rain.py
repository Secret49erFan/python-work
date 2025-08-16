import pygame

import random

from pygame.sprite import Sprite

class Droplet(Sprite):
    '''A class to draw a "Matrix" character'''
    def __init__(self, the_terminal):
        '''Initiate the character attributes'''
        super().__init__()
        self.screen = the_terminal.screen
        self.screen_rect = the_terminal.screen.get_rect()
        # Lo
        self.font = pygame.font.Font('the_matrix/Matrix-Code.ttf', 24)
        self.char = random.choice([chr(i) for i in range(ord('1'), ord('9') + 1)])

#    def _choose_random_char(self):
#        characters = [chr(i) for i in range(ord('1'), ord('9') + 1)]
#        return random.choice(characters)
        
#    def _render_char(self):
#        char = self._choose_random_char()
#        char_surface = self.font.render(self.char, True, (0, 255, 0))
#        return char_surface
    
    def blitme(self):
        char_image = self.font.render(self.char, True, (0, 255, 0))
        self.screen.blit(char_image, (600, 400))