favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f'Hi, {name.title()}.')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}')
favorite_languages['erin'] = 'javascript'
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
else:
    print('Thank you for voting, Erin!')

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')
#############################
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

friends = ['phil', 'sarah']

def greet_friends(favorite_languages, friends):
    for name in favorite_languages.keys():
        print(f'Hi, {name.title()}.')
        if name in friends:
            language = favorite_languages[name].title()
            print(f'\t{name.title()}, I see you love {language}')

def add_new_voter(favorite_languages, name, language):
    if name not in favorite_languages.keys():
        favorite_languages[name] = language
        print(f'{name.title()}, please take our poll!')
    else:
        print(f'Thank you for voting, {name.title()}!')

def thank_voters(favorite_languages):
    for name in sorted(favorite_languages.keys()):
        print(f'{name.title()}, thank you for taking the poll.')

greet_friends(favorite_languages, friends)
add_new_voter(favorite_languages, 'erin', 'javascript')
thank_voters(favorite_languages)
