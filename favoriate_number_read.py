import json

with open('favorite_number.json') as file_object:
    number = json.load(file_object)

print(f"I know your favorite number! It's {number}.")
