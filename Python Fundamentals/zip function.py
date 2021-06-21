# zip function.
"""friends_name = ["Harsh","Sahil","Manthan"]
friends_age  = [25,15,45]

friends_name_age = {
    friends_name[i] : friends_age[i]
    for i in range(len(friends_name))
} """
# Instead Of Above code we can use zip function.

friends_name = ["Harsh","Manthan","Sahil"]
friends_age = [25,49,15]
name_age = dict(zip(friends_name,friends_age))
print(name_age)

# We can do this with the list,set and tuple  also.
name_age_list = list(zip(friends_name,friends_age))
print(name_age_list)

# * in zip
zipped = [("John", 26), ("Anne", 31), ("Peter", 29)]
names, ages = zip(*zipped)

print(names,ages)