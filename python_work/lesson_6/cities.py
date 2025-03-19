# Practice Chapter 6
# Excercise 6-11

cities = { # creating dictionary
    'reno': {'country': 'united states', 'population': 278_226, 'fact': 'biggest little city in the world'},
    'tokyo': {'country': 'japan', 'population': 37_115_000, 'fact': 'shibuya crossing is the world\'s busiest intersection'},
    'rome': {'country': 'italy', 'population': 4_331_970, 'fact': 'nearly 700,000 euros woth of coins are tossed into romes\'s trevi fountain each year'},
}
for city in cities.keys(): # Looping through the keys
    print(f'Name of city: {city.title()}')
    for k, v in cities[city].items(): ### NEED TO USE <ITEMS()> METHOD TO LOOP THRU DICT ITEMS
        if isinstance(v, str): # CHECKS TO SEE IF V IS A STR
            print(f'\t{k.title()}: {v.capitalize()}.') # IF TRUE CAPITALIZE THE STRING
        else:
            print(f'\t{k.title()}: {v}.') # IF FALSE PRINTS THE NUMBER
    print('\n')