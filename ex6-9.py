favorite_places = {
    'lu': ['Tibet', 'Maldives', 'Sanya'],
    'luo': ['Paris', 'Lyon', 'Seattle'],
    'tian': ['Thailan', 'Cambodia']
}

for name, places in favorite_places.items():
    print(name.title() + ' say: "my favorite places is: ')
    for place in places:
        print(place)
    print('"')
