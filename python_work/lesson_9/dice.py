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
        Returns a list of the of dice rolled.
    """
    def __init__(self, sides=6):
        self.sides = sides # initiate attributes

    def roll_die(self, dice=5):
        rolls = [] # create an empty list
        for i in range(dice): # loop 5 times by default
            rolls.append(r(1, self.sides)) # adds roll to the list
        return rolls


my_die = Die() # create an instance of the die class
results = my_die.roll_die()
print(results) # show me the rolls in the console