# Movie Collection App
choice = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'e' to exit: "
movies = []

def add_movie():
    title = input("Enter Movie Title: ")
    director = input("Enter Movie's Director Name: ")
    release_year = input("Enter Release Year Of The Movie: ")
    movies.append(
        {
            "title": title,
            "director": director,
            "release_year": release_year
        }
    )

def show_movies():
    for movie in movies:
        print_movie(movie)


def find_movie():
    search_title = input("Enter Movie Title :")
    for movie in movies:

        if movie["title"] == search_title:
            print_movie(movie)


def print_movie(movie):
    print(f"Movie Name :{movie['title']}")
    print(f"Director Name: {movie['director']}")
    print(f"Release Year: {movie['release_year']}")

user_options = {
      'a': add_movie,
      'l': show_movies,
      'f': find_movie
}


def menu():
    selection = input(choice)
    while selection != 'e':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(choice)

menu()