import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as file_object:
    json.dump(number, file_object)
    print("Thanks! I'll remember that.")
