def show_messages(unreadbooks, readbooks):
    """Display the books to be read, move the books that have already been read into the list"""
    while unreadbooks:
        toread_book = unreadbooks.pop()
        print(f"To read book:{toread_book.title()}")
        readbooks.append(toread_book)


def send_messages(readbooks):
    print("\nThese books have been read: ")
    for readbook in readbooks:
        print(readbook.title())


unbooks = ['python', 'c', 'java']
readbooks = []
show_messages(unbooks, readbooks)
send_messages(readbooks)
print(unbooks)
print(readbooks)
