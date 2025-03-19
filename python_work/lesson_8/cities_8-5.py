# PRACTICE 1/20/25 #
# CHAPTER 8 - CITIES #

def describe_city(city, country='japan'):
    '''RETURN A MESSAGE THAT THE CITY IS IN THE COUNTRY'''
    print(f'{city.title()} is in {country.title()}') # OUTPUT TO THE TERMINAL #

describe_city('tokyo')
describe_city('osaka')
describe_city('rome', 'italy')

farm_animals = [
    "Cow",
    "Pig",
    "Chicken",
    "Sheep",
    "Goat",
    "Horse",
    "Duck",
    "Turkey",
    "Goose",
    "Donkey",
    "Llama",
    "Rabbit",
    "Alpaca",
    "Bee",
    "Guinea Fowl"
]

for animal in farm_animals:
    print(animal)
