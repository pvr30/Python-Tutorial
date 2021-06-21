# sets in python
# sets are define using {}
science_friends = {"Harsh","Manthan","Sahil","Chirag"}
commerce_friends = {"Sanjay","Chirag","Pradip"}

"""# adding a element in set
science_friends.add("Chirag")
print(science_friends)
# Here no duplicate elements in set Sanjay will not print twice.
commerce_friends.add('Sanjay')
print(commerce_friends)

# remove
science_friends.remove("Chirag")

print(science_friends) """


# Some operations on set

# -- Difference --
# Gives you members that are in one set but not the other.

commerce_but_not_science = commerce_friends.difference(science_friends)
science_but_not_commerce = science_friends.difference(commerce_friends)

print(commerce_but_not_science) # {'Sanjay', 'Pradip'}
print(science_but_not_commerce) # {'Harsh', 'Sahil', 'Manthan'}

# -- Symmetric difference --
# Gives you those members that aren't in both sets
# Order doesn't matter with symmetric_difference

not_in_both = commerce_friends.symmetric_difference(science_friends)

print(not_in_both)  # {'Sanjay', 'Manthan', 'Pradip', 'Sahil', 'Harsh'}

# -- Intersection --
# Gives you members of both sets

commerce_and_science = commerce_friends.intersection(science_friends)
print(commerce_and_science)  #  {'Chirag'}

# -- Union --
# Gives you all members of all sets, but of course without duplicates

all_friends = commerce_friends.union(science_friends)
print(all_friends) # {'Harsh', 'Sanjay', 'Chirag', 'Pradip', 'Sahil', 'Manthan'}
