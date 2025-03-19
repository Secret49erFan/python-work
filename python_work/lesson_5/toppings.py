ava_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'pineapple', 'olives']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in ava_toppings:
        print(f'ADDING: {requested_topping}!')
    else:
        print(f'Sorry, we don\'t have {requested_topping} on our menu.')

print('\nYour pizza is now complete!')