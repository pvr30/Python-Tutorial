import json

# converting python to json

info = {
    "Name": "Vishal",
    "Age": 19,             # python dictionary
    "Number": 9081139612
}

temp = json.dumps(info)

print(temp)

# converting json to python

json_info = '{"Name": "Vishal","Age": 19,"Number": 9081139612}'

temp_json = json.loads(json_info)

print(temp_json)


# Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))