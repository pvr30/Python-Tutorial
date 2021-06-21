"""
Mutable: The data that can be changed after created like...
Dictionary, list, set.. almost all

immutable : The data that can't be changed after created like..
int, tuple, float, string .


id() gives you the address of the object
"""
# This is mutable data.
friends = {
    'Harsh': 25,
    'Sahil': 18,
    'Manthan': 20
}

print(id(friends))

friends['Sahil'] = 29

print(id(friends))

friends = {
    'Harsh': 25,
    'Sahil': 18,
    'Manthan': 20
}
print(id(friends)) # here we get different id no because we made different object with same name.


# immutable :

age = 20

print(id(age))

age = 21

print(id(age))

# we get different address

# mutable list example:

my_list = [1, 2, 3, 4]

print(id(my_list))

my_list.append(7)

print(id(my_list))

# we can modify list so it is mutable data

