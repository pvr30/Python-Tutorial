import json

file = open("jsonfile.json", 'r')

# this will convert json file into dictionary.
file_content = json.load(file)
file.close()

print(file_content)

print(file_content["friends"][0])




