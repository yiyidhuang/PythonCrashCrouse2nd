while True:
    age = input("How old are you")
    age = int(age)
    if age < 3:
        print("Free")
    elif age < 12:
        print("The fare is 10 dollar")
    else:
        print("The fare is 15 dollar")
