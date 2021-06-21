headers = ["Name", "Branch", 'CGPA']

info = [
    {"Name": "Vishal", "Branch": "ECE", "CGPA": 6},
    {"Name": "Harsh", "Branch": "BIO", "CGPA": 10},
    {"Name": "Sahil", "Branch": "ECE", "CGPA": 7}
]

import csv

with open("file.csv", 'w') as file:

    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()

    writer.writerows(info)


