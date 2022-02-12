# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"

# name = input(prompt)
# print(f"Hello, {name}!")

# def greet_user():
#    """Display the simple greetings"""
#    print("Hello!")


# greet_user()

# def greet_user(username):
#    """Display the simple greetings"""
#    print(f"Hello, {username.title()}!")


# greet_user('jesse')


def get_formatted_name(first_name, last_name):
    """Return neat name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is a endless while loop
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name == 'q':
        break;
    l_name = input("Last name: ")
    if l_name == 'q':
        break;

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
