import sys

import pygame

from digital_rain import Droplet
from settings import Settings

class Terminal:
    '''Class to define a "Matrix" terminal.'''
    
    def __init__(self):
        '''Initialize the terminal attributes'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.terminal_screen_size) # Set resolution.
        self.rect = self.screen.get_rect()
        pygame.display.set_caption('Matrix Terminal') # Change title.
        
        # Create a Droplet class
        self.drop = Droplet(self)

    def view_simulation(self):
        '''Main loop for the rain.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Fill the screen with color to wipe away last frame.
            self.screen.fill('black')
            
            # Render character to screen.
            self.drop._render_char((600,400))

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
# Make a game instance, and run the game.
    my_terminal = Terminal()
    my_terminal.view_simulation()