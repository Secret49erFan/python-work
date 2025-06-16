from random import randint as r

class Die:
    '''A class to model a n-sided die'''
    def __init__(self, sides=6):
        '''Initiate class attributes.'''
        # Default: six-sided die.
        self.sides = sides

    def roll(self, frequency=1):
        '''Rolls the dice once by default.'''
        rolls = [] # create an empty list
        for i in range(frequency):
            # adds roll to the list
            rolls.append(r(1, self.sides))
        return rolls