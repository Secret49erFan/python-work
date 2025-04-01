import sys

import pygame

from settings import Settings
from circle import Circle

class TheMatrix:
    '''A space where gravity will be simulated.'''

    def __init__(self):
        '''Initialize the matrix and create The One.'''
        pygame.init()
        self.clock = pygame.time.Clock() # Create a clock to set FPS.
        self.settings = Settings() # Create a settings class to manage settings.
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height)) # Sets the width & height of the window.
        self.rect = self.screen.get_rect()
        # Just a label.
        pygame.display.set_caption('The Matrix')

        # Initiate a circle on screen
        self.my_circle = Circle(self.rect.centerx,
                                self.rect.centery,
                                self.settings.cir_radius,
                                self.settings.cir_color,
                                self)
    
    def run_simulation(self):
        '''Begin the simulation.'''
        while True:
            self._check_events()
            self.my_circle.update()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        '''Watch for keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the event type is QUIT then exit gracefuly.
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
#                print(f'The {pygame.key.name(event.key)} key was pressed!')
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            self.my_circle.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.my_circle.moving_left = True
        elif event.key == pygame.K_UP:
            self.my_circle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.my_circle.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.my_circle.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.my_circle.moving_left = False
        elif event.key == pygame.K_UP:
            self.my_circle.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.my_circle.moving_down = False

    def _update_screen(self):
        '''Update images on the screen to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.my_circle.blitme()
        # Essentially refreshes the screen to display the lates drawing updates.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a Matrix and start the simulation.
    the_matrix = TheMatrix()
    the_matrix.run_simulation()