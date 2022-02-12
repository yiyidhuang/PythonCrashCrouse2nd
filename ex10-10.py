def count_common_words(filename, word):
    """Calculate the words in the books."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times"
        print(msg)


filenames = 'alice.txt'

count_common_words(filenames, 'the')
