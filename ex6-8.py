cristiano = {
    'type': 'dog',
    'owner': 'wei',
}

rose = {
    'type': 'cat',
    'owner': 'yan',
}

cloud = {
    'type': 'pig',
    'owner': 'luo',
}

pets = [cristiano, rose, cloud]

for pet in pets:
    if pet == cristiano:
        print('\nCristiano: '
              + '\n\ttype: ' + pet['type']
              + '\n\towner: ' + pet['owner'])
    elif pet == rose:
        print('\nRose: '
              + '\n\ttype: ' + pet['type']
              + '\n\towner: ' + pet['owner'])
    elif pet == cloud:
        print('\nCould: '
              + '\n\ttype: ' + pet['type']
              + '\n\towner: ' + pet['owner'])
