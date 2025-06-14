from random import randint as r

class Die:
    '''A class to model a n-sided die'''
    def __init__(self, sides=6):
        '''Initiate class attributes.'''
        # Default: six-sided die.
        self.sides = sides

    def roll(self, dice=5):
        '''Default five dice rolls.'''
        rolls = [] # create an empty list
        for i in range(dice): # loop 5 times by default
            rolls.append(r(1, self.sides)) # adds roll to the list
        return rolls