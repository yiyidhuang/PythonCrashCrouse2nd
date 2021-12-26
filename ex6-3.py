vocabulary = {
    'for': 'for loop',
    'print': 'print the debug message',
    'pop()': 'remove the data from the end of list',
    'sort()': 'Permanently sorted alphabetically from small to large'
}

# 1
#print(vocabulary)

# 2
# print('for' + ' ' + vocabulary['for'])
# print('print' + ' ' + vocabulary['print'])
# print('pop()' + ' ' + vocabulary['pop()'])
# print('sort()' + ' ' + vocabulary['sort()'])

# 3
for word, value in vocabulary.items():
    print(word + ' : ' + value)
print("\n")
