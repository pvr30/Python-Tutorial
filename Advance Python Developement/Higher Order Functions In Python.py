def greet():
    print('Hello')

def before_and_after(func):
    print('Before...')
    print(func())
    print('After....')

before_and_after(greet)

#before_and_after(5)  # Error

before_and_after(lambda: 5)  # Get 5

# Another Example.

books = [
    {'Name': 'Half GirlFriend', 'Author Name': 'Chetan Bhagat'},
    {'Name': 'Hit Refresh', 'Author Name': 'Satya Nadella'},
    {'Name': 'The Rudest Book Ever', 'Author Name': 'Swetabh Ganwar'}
]

def find_book(expected, finder):
    for book in books:
        if finder(book) == expected:
            return book


find_by = input('Will You Find By Name Or Author Name : ')
looking_for = input('Enter What is your Looking For: ')

print(find_book(looking_for, lambda book: book[find_by]))

