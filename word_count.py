def count_words(filename):
    """Count how many words there are in a file."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# filenames = 'alice.txt'
# count_words(filenames)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
