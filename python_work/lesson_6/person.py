mds = {
    'first_name': 'mike',
    'last_name': 'snodgrass',
    'age': 47,
    'city': 'reno',
}

nlf = {
    'first_name': 'nora',
    'last_name': 'flores',
    'age': 37,
    'city': 'reno',
}

bho = {
    'first_name': 'barack',
    'last_name': 'obama',
    'age': 64,
    'city': 'honolulu',
}

people = [mds, nlf, bho]
    
for person in people:
    print('\n') 
    for k, v in person.items():
        print(f'Key: ({k}) Value: {v}')
#     print(f'Value: {v}')