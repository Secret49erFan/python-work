# practice 2/21/25
# chapter 9
# dice.py

from random import randint as r

class Die:
    """
    A simple class to model a n-sided die.
    Attributes
    ----------
    sides: int
        The number of sides on the die.
    Methods
    -------
    roll_die():
        Returns a list of the number of dice rolled.
    """
    def __init__(self, sides=6):
        self.sides = sides # initiate attributes

    def roll_die(self, dice=5):
        rolls = [] # create an empty list
        for i in range(dice): # loop n times
            rolls.append(r(1, self.sides)) # A number between 1 and n sides.
        return rolls


my_dice = Die() # create an instance of the die class
my_roll = my_dice.roll_die() # add the result of roll to rolls
print(my_roll) # show me the rolls in the console