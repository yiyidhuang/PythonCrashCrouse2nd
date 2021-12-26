name_list = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

received_persons = ['jen', 'phil']
for name in name_list.keys():
    if name in received_persons:
        print("Thank you!" + name.title())
    else:
        print("We invite you !" + name.title())
