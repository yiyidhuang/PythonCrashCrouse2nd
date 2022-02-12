prompt = "How old are you?"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        age = int(message)
        if age < 3:
            print("Free")
        elif age < 12:
            print("The fare is 10 dollar")
        else:
            print("The fare is 15 dollar")
