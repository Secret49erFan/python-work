# practice 2/2/25
# chapter 8 
# Cars

def request_car(make, model, **car):
    '''Builds a car with the requested atributes.'''
    '''Required make and model. Third parameter optional. Creates dictionary.'''
    car['make'] = make
    car['model'] = model
    return car