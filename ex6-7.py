lisa = {
    'first_name': 'li',
    'last_name': 'chen',
    'age': 18,
    'city': 'shenzhen',
}

mary = {
    'first_name': 'wang',
    'last_name': 'fang',
    'age': 25,
    'city': 'hanghzou',
}

jack = {
    'first_name': 'kai',
    'last_name': 'zhang',
    'age': 29,
    'city': 'beijing',
}

leo = {
    'first_name': 'yan',
    'last_name': 'lu',
    'age': 20,
    'city': 'chengdu',
}

# 1
peoples = [lisa, mary, jack, leo]
for person in peoples:
    print(person)

# 2
print("\n================================================\n")
persons = [lisa, mary, jack, leo]
for person in persons:
    print(f"\nName:{person['first_name'].title()}{person['last_name'].title()}")
    print(f"age:{person['age']}")
    print(f"city:{person['city'].title()}")
