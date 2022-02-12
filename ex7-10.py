responses = {}

active = True

while active:
    name = input("\nWhat is your name?")
    response = input('If you could visit one place in the world, where would you go?')

    responses[name] = response
    repeat = input('Would you like to another person response? (yes/no)')
    if repeat == 'no':
        active = False
    print(name.title(), 'would like to ', response)

print(responses)
