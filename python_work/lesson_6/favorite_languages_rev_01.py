favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

friends = ['phil', 'sarah', 'mikey', 'tommy', 'jones']
for name in friends:
#    print(f'Hi, {name.title()}.')
    if name in favorite_languages.keys():
        language = favorite_languages[name]
        print(f'\t{name.title()}, I see you like {language.title()}, but you already polled!')
    else:
        print(f'\tPlease take the poll, {name.title()}!')
# favorite_languages['erin'] = 'javascript'
# if 'erin' not in favorite_languages.keys():
#    print('\nErin, please take our poll!')
# else:
#    print('\nThank you for voting, Erin!')

#for name in sorted(favorite_languages.keys()):
#    print(f'{name.title()}, thank you for taking the poll.')