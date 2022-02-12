filename = 'programming_investigate.txt'

responses = []
while True:
    response = input("\n Why do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

    with open(filename, 'a') as file_object:
        file_object.write(f"{response} \n")
