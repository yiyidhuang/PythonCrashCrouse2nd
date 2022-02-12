# def build_person(first_name, last_name):
#    """Return a dictionary, including the information of one person"""
#    person = {'first': first_name, 'last': last_name}
#    return person


# musician = build_person('jimi', 'hendrix')
# print(musician)

def build_person(first_name, last_name, age=None):
    """Return a dictionary, including the information of one person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
