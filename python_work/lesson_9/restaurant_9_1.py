# practice 2/3/25
# chapter 9
# restaurant class
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

# restaurant1 = Restaurant('smith & river', 'american fusion')
# restaurant2 = Restaurant('perenn', 'cafe')
# restaurant3 = Restaurant('olive garden', 'italian')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
# restaurant.open_restaurant()

# customers_served = restaurant1.number_served # Fetch the current value.
# print(f'{customers_served}') # Output the value to the console.

# restaurant1.number_served = 18 # Change the value to 18 directly.
# customers_served = restaurant1.number_served # Fetch the current value.
# print(f'{customers_served}') # Output the value to the console.

# restaurant1.set_number_served(23) # Change value using the class method.
# customers_served = restaurant1.number_served # Fetch the current value.
# print(f'{customers_served}') # Output the value to the console.
# daily_covers = 87
# restaurant1.increment_number_served(daily_covers)
# print(restaurant1.number_served)
"""
class IceCreamStand(Restaurant):
    '''
    A class to model an ice cream stand inherited from Restaurant.
    
    Attributes
    ----------
    flavors: lst
        The list of flavors available.

    Methods
    -------
    display_flavors():
        Output all flavors to the console.
    '''
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'vanilla',
            'chocolate',
            'strawberry',
            'mint chocolate chip',
            'cookies & cream',
            'rocky road',
            'pistachio'
        ]
    
    def display_flavors(self):
        print("\nToday's available flavors are:")
        for flavor in self.flavors:
            print(f'\t{flavor.title()}')

"""
# my_creamery = IceCreamStand('sundae funday', 'creamery')
# my_creamery.describe_restaurant()
# my_creamery.display_flavors()
