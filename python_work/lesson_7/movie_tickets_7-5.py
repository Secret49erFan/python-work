# PRACTICE 1/14/25 #
# PRACTICE CHAPTER 7 - MOVIE TICKETS #

active= True

prompt = '\nHow many tickets please?' # DEFINE THE PROMPT #
prompt += '\nEnter your age or press "quit" to complete your purchase: '


while active:
    age = (input(prompt))
    if age == 'quit':
        active = False
    else:
        try: # IF THE USER INPUTS A WORD INSTEAD OF A NUMBER - EXCEPT QUIT; ERROR WILL TRIGGER EXCEPTION #
            age = int(age) # ERROR IF WORD NOT NUMBER/QUIT #
            if age <= 2:
                print('Your admission fee is free. Please enjoy the film')
            elif age > 2 and age < 13:
                print('Your admission fee is $10. Please enjoy the film.')
            else:
                print('Your admission fee is $15. Please enjoy the film.')
        except ValueError:
            print('Sorry. Please try again.')