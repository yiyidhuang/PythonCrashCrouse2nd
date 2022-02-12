def show_message(unread_books, read_books):
    """
    List all the book to be read.
    Print the book to be read, move to read_books.
    """
    while unread_books:
        toread_book = unread_books.pop()
        print(f"To read books: {toread_book}")
        read_books.append(toread_book)


def send_message(read_books):
    print('\n:These books have been read : ')
    for book in read_books:
        print(book)


unread_books = ['python', 'java', 'c']
read_books = []
show_message(unread_books, read_books)
send_message(read_books)
