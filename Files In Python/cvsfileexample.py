movies = [
    {"Name": "3 idiots", "Director": "Raju Hirani"},
    {"Name": "Kabir Singh", "Director": "Sandeep Reddy Vanga"},
    {"Name": "Bahubali", "Director": "Raja Mauli"}
]

import csv

# this is called context manager

with open("movies.csv", 'w') as file_write:

    writer = csv.DictWriter(file_write, fieldnames=["Name", "Director"])
    writer.writeheader()
    writer.writerows(movies)



with open("movies.csv", 'r') as file:

    file_content = csv.DictReader(file) # fieldnames=["Name", "Director"])

    for line in file_content:
        print(line)
        print(f"Name: {line['Name']} Director: {line['Director']}")



