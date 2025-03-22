import sys

import pygame

from settings import Settings

class TheMatrix:
    '''A space where gravity will be simulated.'''

    def __init__(self):
        '''Initialize the matrix and create The One.'''
        pygame.init()
        self.clock = pygame.time.Clock() # Create a clock to set FPS.
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('The Matrix') # Just a label.

    def run_simulation(self):
        '''Begin the simualtion.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If the event type is QUIT then exit gracefuly.
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make most recently drawn screen visible.
            pygame.display.flip() # Essentially refreshes the screen to display the lates drawing updates.
            self.clock.tick(24) 

if __name__ == '__main__':
    # Make a Matrix and start the simulation.
    the_matrix = TheMatrix()
    the_matrix.run_simulation()