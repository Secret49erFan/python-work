import sys

import pygame

from settings import Settings

class TheMatrix:
    '''A space where gravity will be simulated.'''

    def __init__(self):
        '''Initialize the matrix and create The One.'''
        pygame.init()
        self.clock = pygame.time.Clock() # Create a clock to set FPS.
        self.settings = Settings() # Create a settings class to manage settings.
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height)) # Sets the width & height of the window.
        pygame.display.set_caption('The Matrix') # Just a label.

    def run_simulation(self):
        '''Begin the simulation.'''
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(24)

    def _check_events(self):
        '''Watch for keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the event type is QUIT then exit gracefuly.
                sys.exit()

    def _update_screen(self):
        '''Update images on the screen to the new screen'''
        self.screen.fill(self.settings.bg_color)
        # Essentially refreshes the screen to display the lates drawing updates.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a Matrix and start the simulation.
    the_matrix = TheMatrix()
    the_matrix.run_simulation()