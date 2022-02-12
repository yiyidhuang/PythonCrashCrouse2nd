def make_album(singer, name, number = ''):
    """Return singers' names and album"""
    album = {'singer': singer, 'name': name}
    if number:
        album['number'] = number

    return album


while True:
    print("\nPlease tell me about the album.")
    print("(enter 'q' to quit")
    singer = input("Singer: ")
    if singer == 'q':
        break
    name = input("Album: ")
    if name == 'q':
        break
    album = make_album(singer, name)
    print(album)
