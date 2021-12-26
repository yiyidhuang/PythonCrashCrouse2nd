favorite_numbers = {
    'lu': list(range(1, 6)),
    'luo': list(range(3, 9)),
    'tom': list(range(0, 8)),
    'andy': list(range(5, 9)),
    'judy': list(range(1, 3)),
}

for name, numbers in favorite_numbers.items():
    print(name + "'s favorite number are:")
    for number in numbers:
        print(number)
