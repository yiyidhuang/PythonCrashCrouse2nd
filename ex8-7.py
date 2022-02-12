def make_album(name, album):
    """Display Singer's name and album"""
    # Define the dictionary
    zj = {'n_name':name, 'a_album':album}

    # Return dictionary
    return zj


mac = make_album('Beyond', 'Amani')
print(mac)

mac = make_album('Adel', 'aAA')
print(mac)

mac = make_album('谭咏麟', '水中花')
print(mac)


def make_album1(name, album, sta=''):
    """Display the singer's name and albums, the optional album numbers"""
    # Define the dictionary
    zj1 = {'n_name1': name, 'a_album1': album}
    # if sta is true, add the sta into the dictionary
    if sta:
        zj1['sta'] = sta
    # Return the dictionary
    return zj1


wc = make_album1('Westlife', 'UK', 'BLue')
print(wc)

wc = make_album1('谭咏麟', '中国', '水中花')
print(wc)

wc = make_album1('Beyond', '中国', '大地')
print(wc)
