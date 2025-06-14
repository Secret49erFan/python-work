from random import choice

class RandomWalk:
    '''A class to generate random walks.'''

    def __init__(self, num_points=5000):
        '''Initialize attributes of a walk.'''
        self.num_points = num_points

        # All walks start at (0.0).
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        '''Calculate all the points in the walk.'''
        # itr = 1
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go.
            # print(f'itr: {itr}')
            # itr += 1
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction*x_distance
            # print(f'xdir: {x_direction} xdis: {x_distance} xstp: {x_step}')

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction*y_distance
            # print(f'ydir: {y_direction} ydis: {y_distance} ystep: {y_step}')

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # print(x)
            # print(f'{y}\n')

            self.x_values.append(x)
            self.y_values.append(y)