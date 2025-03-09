# practice 3/8/25
# chapter 10 - cats and dogs
# cats_and_dogs_10_8.py
from pathlib import Path as p
file_names = ['python_work/Lesson 10/cats.txt',
              'python_work/Lesson 10/snakes.txt',
              'python_work/Lesson 10/dogs.txt',]
for file_name in file_names:
    path = p(file_name)
    try:
        contents = path.read_text()
#        print(f'\nThis is the contents of "{path}":')
#        print(contents)
    except FileNotFoundError:
        pass # Skip non-existent files
#        print(f'\n{path} does not exist.')
    else:
        print(f'\nThis is the contents of "{path}":')
        print(contents)