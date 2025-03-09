# practice 3/8/25
# chapter 10 - addition
# addition_10_6.py
active = True
while active:
    try:
        number_1 = input('What is the first number? Enter "quit" to exit.')
        if number_1.lower() == 'quit':
            active = False
            break
        number_1 = int(number_1)
    except ValueError:
        print('An error has occurred in the first number. Please try again.')
        continue

    while True:
        try:
            number_2 = input('What is the second number? Enter "quit" to exit.')
            if number_2.lower() == 'quit':
                active = False
                break
            number_2 = int(number_2)
            break
        except ValueError:
            print('An error has occurred in the second number. Please try again.')
    if not active:
        break
    
    print(number_1 + number_2)
    break