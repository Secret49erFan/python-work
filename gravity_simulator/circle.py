import pygame

from pygame.sprite import Sprite

class Circle(Sprite):
    '''Simple class to define a circle.'''
    def __init__(self, x, y, radius, color, the_sim):
        '''Initiate pygame and circle attributes.'''
        super().__init__()
        self.screen = the_sim.screen
        self.settings = the_sim.settings
        self.screen_rect = the_sim.screen.get_rect()
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y)) 
        
        # Store a float for the circle's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a circle that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Toggle physics.
        self.physics = False
        self.y_velocity = self.settings.velocity
        
        # Draw the circle to the screen.
        self._draw_circle()
        self.needs_redraw = False
    
    def update(self):
        '''Check for the circle's position and update it.'''
        self._check_movement_flags() # Check for movement flags
        self._simulate_gravity() # Sim the gravity
        self._move_cir_to_top(self.settings.screen_height) # Check for off-screen movement
        
        # Redraw the circle if it needs to be redrawn
        if self.needs_redraw:
            self._update_visuals()

        # Update rect object from self.x and self.y
        self._update_rect_postion()

    def _check_movement_flags(self):
        '''Update the circle's position based on movement flags.'''
        # Update the circle's x and y value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.movement
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.movement
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.movement
        if self.moving_down:
            self.y += self.settings.movement
    
    def _update_rect_postion(self):
        '''Update the circle's rect position.'''
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
    def toggle_physics_flag(self):
        self.physics = not self.physics
    
    def _simulate_gravity(self):
        '''Simulate gravity on the circle.'''
        # Only apply gravity if physics is enabled and the down key is not pressed.
        if self.physics and not self.moving_down:
            # Increase velocity due to gravity
            self.y_velocity += self.settings.gravity
            
            # Cap velocity at terminal velocity to prevent it from going too fast
            if self.y_velocity > self.settings.terminal_velocity: # When y_velocity goes beyound terminal_velocity
                self.y_velocity = self.settings.terminal_velocity # Set it to terminal_velocity cap
            
            # Update the circle's y position based on current velocity
            self.y += self.y_velocity/self.settings.fps
            
    def _move_cir_to_top(self, screen_height):
        '''Moves the circle above the screen if it goes below the screen.'''
        if self.rect.top > screen_height:
            # Move circle to above the screen
            self.rect.bottom = 0
            self.y = self.rect.y
            self.y_velocity = 0 # Reset the velocity to 0
    
    def _stop_cir_at_bottom(self):
        '''Prevent the circle from going below the bottom of the screen'''
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
            self.y = self.rect.y
    
    def _draw_circle(self):
        '''Draw the cir on the surface.'''
        self.image = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def _update_visuals(self):
        '''Update the circle's visuals.'''
        # Redraw the circle
        self._draw_circle()
        self.needs_redraw = False
    
    def blitme(self):
        '''Blit circle to the sim.'''
        self.screen.blit(self.image, self.rect)
