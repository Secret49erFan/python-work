# practice 3/3/25
# chapter 10 - guest
# guest_10_4.py

from pathlib import Path as p # import lib

path = p('python_work/Lesson 10/guest.txt') # path to the file location

prompt = 'What is your name?' # prompt to user
user_name = input(prompt) # capture the name
path.write_text(user_name) # write name to the file
