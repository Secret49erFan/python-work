# practice 2/1/25
# chapter 8 - sandwhiches

def build_sandwiches(*args): # define function with a varied amount of arguments
    print('\nThank you for your order. Let me summarize your ingredients:') # summarize the order
    for ingredient in args: # loop through the arguments
        print(f'\t*{ingredient.title()}') # list ingredients

# call function three times
build_sandwiches('lettuce', 'tomato slices', 'cheddar cheese', 'ham')
build_sandwiches('lettuce', 'swiss', 'ham', 'bacon')
build_sandwiches('lettuce', 'bacon', 'tomato')