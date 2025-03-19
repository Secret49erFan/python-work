# practice 3/12/25
# chapter 10 - favorite number
# favorite_number_10_11b.py
from pathlib import Path as p
import json
path = p('python_work/Lesson 10/favorite_number.json')
content = path.read_text()
favorite_number = json.loads(content)
print(f"I know your favorite number! It's {favorite_number}.")