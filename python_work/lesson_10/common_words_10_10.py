# practice 3/11/25
# chapter 10 - common words
# common_words_10_10.py
from pathlib import Path as p
filenames = ['python_work/Lesson 10/the_adventures_of_sherlock_holmes.txt',
              'python_work/Lesson 10/the_strange_case_of_dr_jekyll_and_mr_hyde.txt',
              'python_work/Lesson 10/the_wonderful_wizard_of_oz.txt',]
for filename in filenames:
    path = p(filename)
    content = path.read_text()
    print(f'\nThe file at {path} has the word "the" about {content.count("the")} times.')