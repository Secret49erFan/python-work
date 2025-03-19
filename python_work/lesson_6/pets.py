pet00 = {
    'name' : 'remi',
    'animal' : 'canine',
    'owner_name' : 'pete',
}

pet01 = {
    'name' : 'lola',
    'animal' : 'canine',
    'owner_name' : 'nora',
}

pet02 = {
    'name' : 'link',
    'animal' : 'feline',
    'owner_name' : 'carla',
}

pet03 = {
    'name' : 'hogan',
    'animal' : 'canine',
    'owner_name' : 'pola',
}

pet04 = {
    'name' : 'waldo',
    'animal' : 'canine',
    'owner_name' : 'nora',
}

pets = [pet00, pet01, pet02, pet03, pet04]

for pet in pets:
    for k, v in pet.items():
        print(f'{k.title()}: {v.title()}')
    print ('\n')