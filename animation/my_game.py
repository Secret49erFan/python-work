import sys

import pygame

class MyGame:
    '''Overall class to manage game assets and behavior.'''
    
    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200,800)) # Set resolution.
        self.rect = self.screen.get_rect()
        pygame.display.set_caption('My Game') # Change title.

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
# Make a game instance, and run the game.
    my_game = MyGame()
    my_game.run_game()