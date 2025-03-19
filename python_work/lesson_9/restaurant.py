class Restaurant:
    '''
    A class to model a restaurant.
    
    Attributes
    ----------
    restaurant_name: str
        The name of the restaurant.
    cuisine_type: str
        The type of restaurant.
    number_served: int
        The number of total covers made by the restaurant.
    
    Methods
    -------
    describe_restaurant():
        Print name and type of restaurant to console.
    open_restaurant():
        Simulates opening of the restaurant.
    set_number_served():
        Set the number of customers served.
    increment_number_served():
        Increment the number of customers serverd by a set amount.
    '''
    
    def __init__(self, restaurant_name, cuisine_type):
        '''Initiating all necessary attributes for the Restaurant object'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        '''Print a neatly formated description of the restaurant'''
        print(f'\nWelcome to {self.restaurant_name.title()}.')
        print(f'Where we serve {self.cuisine_type} food!')

    def open_restaurant(self):
        '''Simulates opening of the restaurant.'''
        print('The restaurant is now open for business.')
    
    def set_number_served(self, covers):
        '''Set the number of customers served.'''
        self.number_served = covers
    def increment_number_served(self, covers):
        '''Increment the number of customers serverd by a set amount.'''
        self.number_served += covers