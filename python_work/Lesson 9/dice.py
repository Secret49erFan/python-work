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

    def roll_die(self):
        result = r(1, self.sides) # A number between 1 and n sides.
        return result


my_die = Die() # create an instance of the die class
rolls = [] # create an empty list
for i in range(3): # loop ten times
    rolls.append(my_die.roll_die()) # add the result of roll to rolls
print(rolls) # show me the rolls in the console