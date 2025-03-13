# practice 3/12/25
# chapter 10 - user dictionary
# user_dictionary_10_13.py
from pathlib import Path
import json


def get_stored_userinfo(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_userinfo(path):
    """Prompt for a new username, number, and color."""
    user_info = {}
    user_info["username"] = input("What is your name? ").strip()
    while True:
        try:
            user_info["fav_number"] = int(input("What is your favorite number: "))
            break
        except ValueError:
            print("There is an error with the number you entered. Please try again.")
    user_info["fav_color"] = input("What is your favorite color: ").strip()
    contents = json.dumps(user_info, indent=4)
    path.write_text(contents)
    return user_info

def greet_user():
    """Greet the user by name."""
    path = Path('python_work/Lesson 10/userinfo.json')
    user_info = get_stored_userinfo(path)
    if user_info:
        print(f"Welcome back, {user_info['username'].title()}!")
        confirm_user = input("Not you? Enter y/n. ")
        if confirm_user == "y":
            print(f"Your number is {user_info['fav_number']}.")
            print(f"Your color is {user_info['fav_color']}.")
        elif confirm_user == "n":
            user_info = get_new_userinfo(path)
            print(f"We'll remember you when you come back, {user_info['username'].title()}!")
        else:
            print("Unexpected Error. Please run program again.")
    else:
        user_info = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {user_info['username'].title()}!")

greet_user()