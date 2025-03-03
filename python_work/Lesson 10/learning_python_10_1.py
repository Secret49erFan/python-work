# practice 2/28/25
# chapter 10
# learning python
import os
from pathlib import Path as p # import lib
print(os.getcwd())
path = p('python_work/Lesson 10/learning_python.txt') # Specify the relative path
contents = path.read_text() # reading whole file
print(contents) # Prints the whole file as is.
print('\n') # Break.

# lines = contents.splitlines() # Reads the file and return list of each line of the file.
for line in contents.splitlines(): # Reiterate through the list.
    print(line) # Print out each line of the file