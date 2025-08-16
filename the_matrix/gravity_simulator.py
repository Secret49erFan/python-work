import sys

import pygame

from settings import Settings
from circle import Circle
from create_circle_grid import CreateCircleGrid

class TheMatrix:
    '''A space where reality will be simulated.'''

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
        self.main_circle = Circle(self.rect.centerx,
                                self.rect.centery,
                                self.settings.cir_radius,
                                self.settings.cir_color,
                                self)
        self.grid_circles = pygame.sprite.Group()
        my_grid = CreateCircleGrid(self)
        my_grid.create_grid(self.grid_circles)
    
    def run_simulation(self):
        '''Begin the simulation.'''
        while True:
            self._check_events()
            self.main_circle.update()
            self.grid_circles.update()
            self._check_collisions() # Between the main circle and grid circles
            self._update_screen()
            self.clock.tick(self.settings.fps)

    def _check_events(self):
        '''Watch for keyboard and mouse events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If the event type is QUIT then exit gracefuly.
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            self.main_circle.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.main_circle.moving_left = True
        elif event.key == pygame.K_UP:
            self.main_circle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.main_circle.moving_down = True
        

    def _check_keyup_events(self, event):
        '''Respond to keypresses'''
        if event.key == pygame.K_RIGHT:
            self.main_circle.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.main_circle.moving_left = False
        elif event.key == pygame.K_UP:
            self.main_circle.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.main_circle.moving_down = False
        elif event.key == pygame.K_p:
            self.main_circle.toggle_physics_flag()
            for circle in self.grid_circles:
                circle.toggle_physics_flag()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_collisions(self):
        '''Check for collisions between the main circle and grid circles.'''
        # Check for collisions with the main circle and grid circles
        collisions = pygame.sprite.spritecollide(self.main_circle, self.grid_circles, False)
        if collisions:
            for circle in collisions:
                self._handle_collision(circle)
                
    def _handle_collision(self, circle):
        '''Handle the collision between the main circle and grid circles.'''
        self.grid_circles.remove(circle)

    def _update_screen(self):
        '''Update images on the screen to the new screen'''
        self.screen.fill(self.settings.bg_color)
        self.grid_circles.draw(self.screen)
        self.main_circle.blitme()
        # Essentially refreshes the screen to display the lates drawing updates.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a Matrix and start the simulation.
    the_matrix = TheMatrix()
    the_matrix.run_simulation()