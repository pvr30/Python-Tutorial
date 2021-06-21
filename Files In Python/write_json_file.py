# json = javascript object notation
import json

info = [
    {
        "Name": "Vishal",
        "Branch": "ECE",
        "CGPA": 6
    }
]

file = open("jsonfile.json", 'w')

# this will put the info in jsonfile
json.dump(info, file)

file.close()





