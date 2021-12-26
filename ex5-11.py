ordinal_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for ordinal_num in ordinal_nums:
    if ordinal_num == '1':
        print("1" + "st")
    elif ordinal_num == '2':
        print("2" + "nd")
    elif ordinal_num == '3':
        print("3" + "rd")
    else:
        print(ordinal_num + "th")
