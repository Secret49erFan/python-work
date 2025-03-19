rivers = {
    'thames': 'london',
    'seine': 'paris',
    'vltava': 'czech republic',
}

for river, city in rivers.items(): # REMINDER: When iterating over a dict; use items() #
    print(f'The {river.title()} runs through {city.title()}.')

for river in rivers.keys():
    print(river)

for city in rivers.values():
    print(city)
