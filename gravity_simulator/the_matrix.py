import sys

import pygame

from random import randint as r

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
        self.main_circle = Circle(self.rect.centerx,
                                self.rect.centery,
                                self.settings.cir_radius,
                                self.settings.cir_color,
                                self)
        self.grid_circles = pygame.sprite.Group()
        self._create_grid()
    
    def run_simulation(self):
        '''Begin the simulation.'''
        while True:
            self._check_events()
            self.main_circle.update(self.grid_circles)
            self.grid_circles.update(self.grid_circles)
            self._update_screen()
            self.clock.tick(self.settings.fps)


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
            self.main_circle.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.main_circle.moving_left = True
        elif event.key == pygame.K_UP:
            self.main_circle.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.main_circle.moving_down = True
        elif event.key == pygame.K_p:
            self.main_circle.toggle_physics_flag()
            for circle in self.grid_circles:
                circle.toggle_physics_flag()
        elif event.key == pygame.K_q:
            sys.exit()

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

    def _create_grid(self):
        '''Create the grid of cicles.'''
        # Create a circle and keep adding circles until there's no room left.
        # Spacing between circles in ten circle widths and ten circle heights.
        grid_circle = Circle(self.settings.grid_cir_radius*self.settings.grid_padding,
                             self.settings.grid_cir_radius*self.settings.grid_padding,
                             self.settings.grid_cir_radius,
                             self.settings.grid_cir_color,
                             self)
        circle_width, circle_height = grid_circle.rect.size
        current_x, current_y = circle_width, circle_height
        while current_y < (self.settings.screen_height - self.settings.grid_padding * circle_height):
            while current_x < (self.settings.screen_width - self.settings.grid_padding * circle_width):
                self._create_circle_for_grid(current_x+r(-self.settings.jitter,
                                                          self.settings.jitter),
                                             current_y+r(-self.settings.jitter,
                                                          self.settings.jitter))
                current_x += self.settings.grid_padding * circle_width

            # Finish a row; reset x value and increment y value.
            current_x = circle_width
            current_y += self.settings.grid_padding * circle_height

    
    def _create_circle_for_grid(self, x_position, y_position):
        '''Create a circle and place it in grid.'''
        new_circle = Circle(x_position,
                            y_position,
                            self.settings.grid_cir_radius,
                            self.settings.grid_cir_color,
                            self)
        new_circle.x = x_position
        new_circle.y = y_position
        new_circle.rect.x = x_position
        new_circle.rect.y = y_position
        self.grid_circles.add(new_circle)
        

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