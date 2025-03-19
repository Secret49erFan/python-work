fav_numbs = {
    'alex': [7, 2, 4, 24],
    'mikey': [11, 18],
    'nora': [8, 9, 10],
    'janet': [5],
    'joann': []
    }

for nas, nus in fav_numbs.items():
    if len(nus) == 0:
        print(f'{nas.title()} doesn\'t have any favorite numbers:')
    elif len(nus) == 1:
        print(f'{nas.title()}\'s favorite number is:')
    else:
        print(f'{nas.title()}\'s favorite numbers are:')
    for nu in nus:
        print(f'\t{nu}')