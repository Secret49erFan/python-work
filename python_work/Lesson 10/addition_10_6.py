# practice 3/8/25
# chapter 10 - addition
# addition_10_6.py
active = True
number_1 = 0
number_2 = 0
while active:
    try:
        number_1 = int(input('What is the first number?'))
        number_2 = int(input('What is the second number?'))
        break
    except ValueError:
        print("An error has occured. Please try again")

print(number_1 + number_2)