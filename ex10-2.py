filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    # Delete line breaks at the end of a line, then replace python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
