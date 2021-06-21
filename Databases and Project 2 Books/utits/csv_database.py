import csv
books_file = "books_cvs.csv"

def add(name, author_name):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author_name},0\n")

def show():
    with open(books_file, 'r') as file:
        books = [line.strip().split(',') for line in file.readlines()]

    return [
        {'Name': book[0], 'Author Name': book[1], 'Read': book[2]}
        for book in books
    ]

def _save_file_content(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['Name']},{book['Author Name']},{book['Read']}\n")


def read(name):
    books = show()
    for book in books:
        if book['Name'] == name:
            book['Read'] = '1'

    _save_file_content(books)


def delete(name):
    books = show()
    for book in books:
        if book['Name'] == name:
            books.remove(book)

    _save_file_content(books)