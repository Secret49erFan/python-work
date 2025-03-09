# practice 3/3/25
# chapter 10 - guest book
# guest_book_10_5.py
from pathlib import Path as p # import lib

active = True
prompt = 'Please enter the names of all your guests.'
prompt += '\nEnter "quit" when finished.'

list_of_names = '' # create empty string

while active:
    user_name = input(f'{prompt}\n')
    if user_name.lower() == 'quit':
        active = False
    else:
        list_of_names += user_name + '\n'

path = p('python_work/Lesson 10/guest_book.txt')
path.write_text(list_of_names)