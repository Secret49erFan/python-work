from random import randint as r

from circle import Circle

class CreateCircleGrid:
    '''A class to generate a grid of circles'''
    def __init__(self, the_sim):
        self.settings = the_sim.settings
        self.sim = the_sim

    def create_grid(self, circle_group):
        '''Create a grid of circles in a single function.'''
        # Determine spacing between circles
        circle_width = self.settings.grid_cir_radius * 2
        circle_height = self.settings.grid_cir_radius * 2
        current_x, current_y = circle_width, circle_height

        while current_y < (self.settings.screen_height - self.settings.grid_padding * circle_height):
            while current_x < (self.settings.screen_width - self.settings.grid_padding * circle_width):
                # Create a new circle and place it in the grid
                x_position = current_x + r(-self.settings.jitter, self.settings.jitter)
                y_position = current_y + r(-self.settings.jitter, self.settings.jitter)
                new_circle = Circle(x_position,
                                    y_position,
                                    self.settings.grid_cir_radius,
                                    self.settings.grid_cir_color,
                                    self.sim)
                new_circle.x = x_position
                new_circle.y = y_position
                new_circle.rect.x = x_position
                new_circle.rect.y = y_position

                # Add the circle to the grid
                circle_group.add(new_circle)
            
                # Move to the next column
                current_x += self.settings.grid_padding * circle_width

            # Reset x position and move to the next row
            current_x = circle_width
            current_y += self.settings.grid_padding * circle_height