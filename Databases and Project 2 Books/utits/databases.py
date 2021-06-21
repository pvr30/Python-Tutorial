books = []

def add(name, author_name):
    books.append({"Name": name, "Author Name": author_name, "Read": False})


def read(name):
    for book in books:
        if book['Name'] == name:
            book['Read'] = True

def show():
    return books

def delete(name):
    for book in books:
        if name == book['Name']:
            books.remove(book)
