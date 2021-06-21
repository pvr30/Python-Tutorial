import json
book_file = "books_json.json"

with open(book_file, 'w') as file:
    json.dump([], file)

def show():
    with open(book_file, 'r') as file:
        return json.load(file)


def add(name, author_name):
    books = show()
    books.append({"Name": name, "Author Name": author_name, "Read": False})
    _save_file_content(books)

def _save_file_content(books):
    with open(book_file, 'w') as file:
        json.dump(books, file)


def read(name):
    books = show()
    for book in books:
        if book['Name'] == name:
            book['Read'] = True
    _save_file_content(books)

def delete(name):
    books = show()
    for book in books:
        if book['Name'] == name:
            books.remove(book)
    _save_file_content(books)