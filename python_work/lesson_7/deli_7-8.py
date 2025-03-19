# PRACTICE 1*15*25 #
# CHAPTER 7 - DELI #

# MAKE LIST OF ORDERS #
sandwich_orders = ['capastrami', 'the bobby', 'capastrami', 'cheese steak', 'capastrami']
# MAKE EMPTY LIST 
finished_sandwiches = []

while sandwich_orders: # AS LONG AS THE LIST IS NOT EMPTY THIS WILL BE TRUE #
    current_sandwich = sandwich_orders.pop() # POP-OFF THE LAST ITEM IN LIST AND LABEL IT #
    if current_sandwich == 'capastrami':
        print(f'Shiiit! We ran out of {current_sandwich.title()}')
    else:
        print(f'Your order of {current_sandwich.title()} is coming right up!') # LET THE CUSTOMER KNOW YOU'RE WORKING ON THEIR SANDWICH #
        finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)