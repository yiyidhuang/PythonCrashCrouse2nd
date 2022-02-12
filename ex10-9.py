filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)
