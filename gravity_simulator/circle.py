import pygame

class Circle:
    '''Simple class to define a circle.'''
    def __init__(self, x, y, radius, color, the_sim):
        '''Initiate pygame and circle attributes.'''
        self.screen = the_sim.screen
        self.screen_rect = the_sim.screen.get_rect()
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y)) 
        
        # Draw circle to the new surface.
        pygame.draw.circle(self.image, color, (radius, radius), radius) # can this be defined in a method???

    def blitme(self):
        '''Draw circle'''
        self.screen.blit(self.image, self.rect)