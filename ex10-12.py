import json

try:
    with open('favorite_number.json') as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as file_object:
        json.dump(number, file_object)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.")
