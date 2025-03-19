# practice 3/12/25
# chapter 10 - favorite number remembered
# favorite_number_remembered_10_12.py
from pathlib import Path as p
import json
path = p('python_work/Lesson 10/favorite_number_remembered.json')
if path.exists():
    content = path.read_text()
    favorite_number = json.loads(content)
    print(f"I know your favorite number! It's {favorite_number}.")
else:
    favorite_number = input('Enter your favorite number: ')
    content = json.dumps(favorite_number)
    path.write_text(content)