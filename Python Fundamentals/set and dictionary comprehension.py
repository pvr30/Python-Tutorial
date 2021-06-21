# set comprehension
friends = ["Harsh","Manthan","Sahil"]
friends_lower = {name.lower() for name in friends}
print(friends_lower)
# This is nothing different than list.

# Dictionary Comprehension
# Works just like set comprehension,
# but you need to do key-value pairs.
friends_name = ["Harsh","Sahil","Manthan"]
friends_age  = [25,15,45]

friends_name_age = {
    friends_name[i] : friends_age[i]
    for i in range(len(friends_name))
}
print(friends_name_age)