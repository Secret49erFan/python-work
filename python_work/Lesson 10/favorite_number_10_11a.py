# practice 3/12/25
# chapter 10 - favorite number
# favorite_number_10_11a.py
from pathlib import Path as p
import json
path = p('python_work/Lesson 10/favorite_number.json')
favorite_number = input('Enter your favorite number: ')
content = json.dumps(favorite_number)
path.write_text(content)