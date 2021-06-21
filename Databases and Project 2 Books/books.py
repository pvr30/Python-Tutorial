from utits import databases
from utits import csv_database
from utits import json_databases
from utits import SQL_databases
input_form = """
1.Enter 'a' for add a book in a list.
2.Enter 'r' for read a book from list.
3.Enter 's' to show all books from list.
4.Enter 'd' to delete a book from a list.
5.Enter 'q' to quit from this app.
Your Choice:
 """
def main():
    user_input = input(input_form)
    while user_input != 'q':
        if user_input == 'a':
            add_book()
        elif user_input == 'r':
            read_book()
        elif user_input == 's':
            show_book_list()
        elif user_input == 'd':
            delete_book()
        else:
            print("Enter Valid Command")
        user_input = input(input_form)

def add_book():
    name = input("Enter Book Name: ")
    author_name = input("Enter Author Name: ")

    #databases.add(name, author_name)
    #csv_database.add(name, author_name)
    #json_databases.add(name, author_name)
    SQL_databases.add(name, author_name)

def read_book():
    name = input("Enter Book Name: ")
    #databases.read(name)
    #csv_database.read(name)
    #json_databases.read(name)
    SQL_databases.read(name)

def show_book_list():
    #get_books = databases.show()
    #get_books = csv_database.show()
    #get_books = json_databases.show()
    get_books = SQL_databases.show()
    for book in get_books:
        #read = 'Yes' if book['Read'] == '1' else 'No'
        read = 'Yes' if book['Read'] else 'No'
        print(f"ID: {book['ID']}, Name: {book['Name']}, Author Name: {book['Author Name']}, Read: {read} ")


def delete_book():
    name = input("Enter Book Name: ")
    #databases.delete(name)
    #csv_database.delete(name)
    #json_databases.delete(name)
    SQL_databases.delete(name)


main()