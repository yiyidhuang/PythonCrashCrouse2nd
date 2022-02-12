import json

# username = input("What is your name? ")

# filename = 'username.json'
# with open(filename, 'w') as file_object:
#    json.dump(username, file_object)
#    print(f"We'll remember you when you come back, {username}!")

# filename = 'username.json'
# try:
#    with open(filename) as file_object:
#        username = json.load(file_object)
# except FileNotFoundError:
#    username = input("What is your name? ")
#    with open(filename, 'w') as file_object:
#        json.dump(username, f)
#        print(f"We'll remember you when you come back, {username}")
# else:
#    print(f"Welcome back, {username}!")


# def greet_user():
#    filename = 'username.json'
#    try:
#        with open(filename) as file_object:
#            username = json.load(file_object)
#    except FileNotFoundError:
#        username = input("What is your name? ")
#        with open(filename, 'w') as file_object:
#            json.dump(username, file_object)
#            print(f"We'll remember you when you come back, {username}!")
#    else:
#        print(f"Welcome back, {username}!")


# greet_user()


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        #username = input("What is your name? ")
        #filename = 'username.json'
        #with open(filename, 'w') as file_object:
        #    json.dump(username, file_object)
        #    print(f"We'll remember you when you come back, {username}!")
        if username:
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")


greet_user()


