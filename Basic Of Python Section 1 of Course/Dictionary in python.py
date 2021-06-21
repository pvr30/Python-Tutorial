# Dictionary in python
# Dictionary in Python is an unordered collection of data values, used to store data values like a map,
# which unlike other Data Types that hold only single value as an element,
# Dictionary holds key:value pair.
# Key value is provided in the dictionary to make it more optimized.
friends_age = {"Harsh":21,"Sahil":18,"Manthan":19}
print(friends_age)
print(friends_age["Harsh"])
print(friends_age["Sahil"])

# Modifying existing keys
friends_age["Manthan"] = 45
# friends_age["Manthan":45] # Error
print(friends_age)

# Adding a new key in dictionary
friends_age["Sanjay"] = 10
print(friends_age["Sanjay"])
print(friends_age)


# -- Lists of dictionaries --
# Imagine you have a program that stores information about your friends.
# This is the perfect place to use a list of dictionaries.
# That way you can store multiple pieces of data about each friend, all in a single variable.

friends = [
    {"name":"Harsh","age":25},
    {"name":"Sahil","age":18},
    {"name":"Manthan","age":50}
]
print(friends[0]["name"])
print(friends[2]["age"])
print(friends)

# dict function to convert in dictionary

subject_code = [("Maths",304),("Physics",209),("Chemistry",100)]
subject = dict(subject_code)
print(subject)
print(subject["Chemistry"])