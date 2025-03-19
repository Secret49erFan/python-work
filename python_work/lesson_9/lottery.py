# practice 2/23/25
# chapter 9-14
# lottery.py

from random import choice as c
lottery_pull = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E')

def generate_ticket(digits=4):
    random_numbers = []
    for i in range(digits):
        random_numbers.append(c(lottery_pull))
    return random_numbers
list_of_tickets = []
# my_ticket = ['A', 4, 2, 4]
my_ticket = generate_ticket()
rolling = True
iterations = 0
while rolling:
    current_ticket = generate_ticket()
    if my_ticket == current_ticket:
        print(f"The winning numbers for this lottery are: {current_ticket}.")
        rolling = False
    else:
        iterations += 1
        list_of_tickets.append(current_ticket)
# print(len(list_of_tickets))
# print(c(list_of_tickets))
print(f"Your odds of winning were 1 in {iterations}!")