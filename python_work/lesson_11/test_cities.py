# practice 3/17/25
# chapter 11 - city, country
# test_cities.py
from city_functions import city_country
def test_city_country():
    '''Does the city and country return formatted'''
    formatted_city = city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'