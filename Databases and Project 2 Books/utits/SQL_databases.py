
"""
SQL - Structured Query Language
It A a database where we can interact with data in table form.
first we have to connect sqlit3 to database(.db) file
cursor() is used for pointing the row from the table we made
the sql is ENGLISH liked Language.
cursor.execute() is used to define and do our task to store data.
connection.commit() is used to save our data in database file.
cursor.fechall() is used to return the data .
we have close the connection after doing task.
"""

"""
import sqlite3

def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(id integer primary key,name text,author text,read integer default 0)')

    connection.close()


def add(name, author_name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books(name, author) VALUES(?, ?)', (name, author_name))
    connection.commit()
    connection.close()

def show():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')

    books = [{"ID": row[0], "Name": row[1], "Author Name": row[2], "Read": row[3]} for row in cursor.fetchall()]

    connection.close()
    return books

def read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    connection.commit()
    connection.close()

def delete(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()

"""
"""
Below method is called context manager:
Here we don't need to close or commit file .
"""

from .SQL_databases_connection import DatabaseConnection


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(id integer primary key,name text,author text,read integer default 0)')


def add(name, author_name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books(name,author) VALUES(?,?)', (name, author_name))

def show():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')

        books = [{"ID": row[0], "Name": row[1], "Author Name": row[2], "Read": row[3]}
                 for row in cursor.fetchall()]

    return books


def read(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read="1" WHERE name=?', (name,))

def delete(name):
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))

