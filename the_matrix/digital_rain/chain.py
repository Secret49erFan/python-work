import pygame

import random

from droplet import Droplet

class Chain:
    '''A class to create a chain of characters'''
    def __init__(self, the_terminal) -> None:
        '''Initiate the chain attributes'''
        # Create an instance of the Terminal class.
        self.terminal = the_terminal
        # Amount of droplets to generate.
        self.length_of_chain = self._gen_rand_droplets()
        self.droplets = pygame.sprite.Group()
        # This will be random after testing rendering.
        self.x_pos = self._gen_rand_x_pos()
        self.y_pos = self._gen_rand_y_pos()
        self._generate_chain()
    
    def update(self) -> None:
        '''Update and draw the droplets in the chain'''
        for droplet in self.droplets: # A sprite group.
            # Check each dropet's pos with its own update() method
            droplet.update()
        # Blit entire sprite group to the terminal screen.
        self.droplets.draw(self.terminal.screen)

    def _generate_chain(self) -> None:
        '''Create a chain of "Matrix" characters of random n size.'''
        for droplet in range(self.length_of_chain):
            # Create instance of Droplet and add the droplet to the sprite group
            droplet = Droplet(self.terminal)
            self.droplets.add(droplet)
            # Get the height of droplet for spacing.
            char_height = int(droplet.char_height)
            # Get and set the inital rect of the base droplet.
            droplet.rect.y = self.y_pos - char_height
            droplet.rect.x = self.x_pos
            # Update base y pos to create stacking effect.
            self.y_pos -= char_height

    def _gen_rand_droplets(self) -> int:
        '''Return a random number for droplet generation.'''
        return random.randint(self.terminal.settings.min_chain_length, self.terminal.settings.max_chain_length)
    
    def _gen_rand_x_pos(self) -> int:
        '''Return a random x-pos for the chain.'''
        return random.randint(0, self.terminal.rect.width)
    
    def _gen_rand_y_pos(self) -> int:
        '''Return a randon y-pos for the chain.'''
        return -random.randint(0, self.terminal.settings.max_chain_height)