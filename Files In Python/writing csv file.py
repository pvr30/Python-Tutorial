headers = ["Name", "Branch", 'CGPA']

info = [
    ["Vishal", "ECE", 6.3],
    ["Harsh", "BM", 7.9],
    ["Sahil", "CSE", 9]
]
import csv

with open("file.csv", 'w') as file:

    writer = csv.writer(file)

    writer.writerow(headers)

    writer.writerows(info)


# writerow(): This method writes a single row at a time.
# writerows(): This method is used to write multiple rows at a time.

