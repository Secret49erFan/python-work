# PRACTICE 1/14/25 #
# PRACTICE CHAPTER 7 - PIZZA TOPPINGS #

active = True # SET TO TRUE

prompt = '\nEnter your desired topping.' # DEFINE THE PROMPT #
prompt += '\n(Continue entering toppings. Enter "quit" when finished.)'

while active: # ENTER THE LOOP AS LONG AS <active> IS TURE #
    topping = input(prompt)
    if topping != 'quit': # IF THE RESPONSE IS NOT <quit>, PRINT TOPPING #
        print(f'{topping} has been added to your pizza.')
    else:
#         break
        active = False # IF THE REPSONSE IS <quit>; EXIT THE LOOP #