# 12/21/24
# python practice
fav_pizzas = ['perpperoni', 'supreme', 'hawai\'ian', 'meat lovers', 'margherita'] # initiate list
for pizza in fav_pizzas: # initiate loop
    print(f'I fucking love {pizza} pizza!') # print the name each pizza w/message
print('I like pizza a lot.\n')
print('The first three items in the list are:')
for pizza in fav_pizzas[:3]:
    print(pizza)
print('\nThe items from the middle of the list are:')
for pizza in fav_pizzas[1:4]:
    print(pizza)
print('\nThe last three items in the list are:')
for pizza in fav_pizzas[-3:]:
    print(pizza)
frd_pizzas = fav_pizzas[:]
fav_pizzas.append('cheese')
frd_pizzas.append('neopolitan')
print('\nMy favorite pizzas are:')
for pizza in fav_pizzas:
    print(pizza)
print('\nMy friends favorite pizzas are:')
for pizza in frd_pizzas:
    print(pizza)