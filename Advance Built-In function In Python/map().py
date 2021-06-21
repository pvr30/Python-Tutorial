#The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.


num_list = ['2', '3', '10', '9']

print(list(map(int, num_list)))

# It will convert the string element of list into int

friends = ['Harsh', 'Sahil', 'Manthan', 'Sanjay']

friends_lower = map(lambda name: name.lower(), friends)

print(friends_lower)
print(list(friends_lower))

# Also We can do like this.
friends_upper = [name.upper() for name in friends ]
print(friends_upper)

# We can use Generator Comprehension also
another_friends = (name.upper() for name in friends)

print(another_friends)
print(list(another_friends))