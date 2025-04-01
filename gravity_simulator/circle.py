import pygame

class Circle:
    '''Simple class to define a circle.'''
    def __init__(self, x, y, radius, color, the_sim):
        '''Initiate pygame and circle attributes.'''
        self.screen = the_sim.screen
        self.settings = the_sim.settings
        self.screen_rect = the_sim.screen.get_rect()
        self.x = x
        self.y = y
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

    def update(self):
        '''Update the circle's position based on movement flags.'''
        # Update the circle's x value not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.movement
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.movement
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.movement
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.movement
        
        # Sim the gravity
        self.y += self.settings.gravity
        
        # Prevent the circle from going below the bottom of the screen
        if self.rect.bottom > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom
            self.y = self.rect.y

        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_circle(self):
        '''Draw a circle '''
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
    
    def blitme(self):
        '''Blit circle to the sim.'''
        self.draw_circle()
        self.screen.blit(self.image, self.rect)