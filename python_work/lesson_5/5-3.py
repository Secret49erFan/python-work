
alien_color = 'red' # set the color

# if alien_color == 'green':
#     print('You earned 5 points')
# if alien_color == 'red':
#     print('You earned 5 points')
# if alien_color == 'green':
#     print('You earned 5 points.')
# else:
#     print ('You earned 10 points.')
# if alien_color == 'red':
#     print('You earned 5 points.')
# else:
#     print ('You earned 10 points.')

if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print('You earned 10 points')
else:
    print('You earned 15 points')
# // ---->
alien_color = 'green' #change the color
if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print('You earned 10 points')
else:
    print('You earned 15 points')
# // ---->
alien_color = 'yellow' #change the color
if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print('You earned 10 points')
else:
    print('You earned 15 points')

## WHATS YOUR AGE ##
age = int(input('What\'s your age?')) # INPUT from the user AND convert str --> int ***
if age < 2:
    print('You are a baby.')
elif age < 4:
    print('You are a todler.')
elif age < 13:
    print('You are a kid.')
elif age < 20:
    print('You are an teenager.')
elif age < 65:
    print('You are an adult.')
else:
    print('You are an elder.')

## WHATS YOU FAVORITE FRUIT ##
favorite_fruit = ['raspberry', 'kiwi', 'mango']
if 'kiwi' in favorite_fruit:
    print('You realy like kiwis!')
if 'orange' in favorite_fruit:
    print('You really like oranges!')
if 'mango' in favorite_fruit:
    print('You really like mangos!')
if 'apple' in favorite_fruit:
    print('You really like apples!')
if 'raspberry' in favorite_fruit:
    print('You really like raspberries!')