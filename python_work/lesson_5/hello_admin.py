current_users = ['Admin', 'AFlores', 'MSnodgrass', 'NFlores', 'JRamirez']
new_users = ['Admin', 'JSnodgrass', 'SMoffit', 'ABarajas', 'AFlores']
lower_current_users = [current_user.lower() for current_user in current_users] # one-line for loop to lower case items from the current_users list
print(lower_current_users)

if new_users:
    for new_user in new_users:
        if new_user.lower() in lower_current_users: # IF THIS DOESN'T WORK; TRY 'IN' INSTEAD OF THE '==' OPERATOR #
            print(f'{new_user.lower()} not available. Please enter a new username.')
        else:
            print(f'The username: {new_user.lower()} is available.')

numbs = list(range(1,10))
print(numbs)
for numb in numbs:
    if numb == 1:
        print(f'{numb}st')
    elif numb == 2:
        print(f'{numb}nd')
    elif numb == 3:
        print(f'{numb}rd')
    else:
        print(f'{numb}th')