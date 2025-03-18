# practice 3/17/25
# chapter 11 - city, country
# test_cities.py
from city_functions import city_country
def test_city_country():
    '''Does the city and country format correctly without a population.'''
    formatted_str = city_country('santiago', 'chile')
    assert formatted_str == 'Santiago, Chile'

def test_city_country_population():
    '''Does the city, country, and population return formatted.'''
    formatted_str = city_country('santiago', 'chile', '5000000')
    assert formatted_str == 'Santiago, Chile -- Population 5000000'