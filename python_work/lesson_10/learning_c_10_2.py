# practice 3/2/25
# chapter 10 - learning c
# learning_c_10_2.py
from pathlib import Path as p
path = p('python_work/Lesson 10/learning_python.txt')
contents = path.read_text()
# lines = contents.splitlines()
print(contents)
for line in contents.splitlines():
    line = line.replace('python', 'c')
    print(line)