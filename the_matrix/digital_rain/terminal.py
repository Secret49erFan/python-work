import sys

import pygame

from chain import Chain
from terminal_settings import Settings

class Terminal:
    '''Class to define a "Matrix" terminal.'''
    
    def __init__(self):
        '''Initialize the terminal attributes'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.terminal_screen_size) # Set resolution.
        # Get a rectangle of the screen itself.
        self.rect = self.screen.get_rect()
        pygame.display.set_caption('Matrix Terminal') # Set a window title.
        # Create a group of chain instances.
        # What: Call Chain()
        # How: 7 times with range(0-6)
        # When: (NA) Always
        self.chains = [Chain(self) for _ in range(self.settings.num_of_chains)]
        
    def view_simulation(self):
        '''Main loop for the rain.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Fill the screen with color to wipe away last frame.
            self.screen.fill('black')
            
            # Render chains to screen.
            for chain in self.chains:
                chain.update()
           
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(self.settings.fps)

if __name__ == '__main__':
# Make a game instance, and run the game.
    my_terminal = Terminal()
    my_terminal.view_simulation()