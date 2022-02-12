def show_messages(books):
    """print books to be read"""
    for book in books:
        message = f"To read book:{book.title()}"
        print(message)


toread_books = ['python', 'java', 'c']
show_messages(toread_books)
