favorite_numbers = {
    'alice': '7',
    'tom': '8',
    'andy': '9',
    'rose': '10',
    'frank': '26'
}

# 1
# print(favorite_numbers)

# 2
# print("Alice's favorite number is " + str(favorite_numbers['alice']))
# print("Tom's favorite number is " + str(favorite_numbers['tom']))
# print("Andy's favorite number is " + str(favorite_numbers['andy']))
# print("Rose's favorite number is " + str(favorite_numbers['rose']))
# print("Frank's favorite number is " + str(favorite_numbers['frank']))

# 3
for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite number is " + str(numbers) + ".")
