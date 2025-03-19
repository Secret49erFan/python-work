age = input('What\'s your age?') # INPUT from the user ***
if int(age) >= 18: # checks if the INPUT is greater than or equal to 18
    print('You are of age to vote. Do your duty!') # if 18 or older
    print('Have you registered to vote yet?') # same ^^^
else:
    print('You are too young!') # if 17 or under
    print('Register as soon as you turn 18!') # same ^^^