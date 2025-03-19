"""
# PRACTICE 1*15*25 #
# CHAPTER 7 - DREAM VACATION #
"""
polling_active = True # POLL ACTIVE WHILE THIS IS TRUE #
poll_results = {} # MAKE EMPTY DICT #

while polling_active:
    name = input('Enter your name for the poll.')
    destination = input('What is your dream destination anywhere in the world?')
    end_poll = input('Enter another name? Enter yes/no.')
    poll_results[name] = destination
    if end_poll == 'no':
        polling_active = False
print('\nAnd the results are in!! This is where y\'all want to go!')
for k, v in poll_results.items():
    print(f'{k.title()}: {v.title()}')