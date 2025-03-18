# practice 3/17/25
# chapter 11 - city, country
# city_functions.py
def city_country(city, country, population=''):
    if population:
        formatted_str = f'{city}, {country} -- population {population}'
    else:
        formatted_str = f'{city}, {country}'
    return formatted_str.title()