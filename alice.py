filename = 'alice.txt'

# with open(filename, encoding='utf-8') as file_object:
#    contents = file_object.read()

try:
    with open(filename, encoding='utf-8') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Calculate the numbers of words
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
