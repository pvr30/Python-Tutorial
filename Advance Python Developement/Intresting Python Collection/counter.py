"""
Counter: It Gives How many duplicates .
Allows us to count things. Give it a iterable or a
mapping (such as a dict) and it will turn into a counter of elements.

"""
from collections import Counter

friends = ['Harsh', 'Sahil', 'Manthan', 'Chirag', 'Harsh', 'Manthan', 'Manthan', 'Sahil']

friends_count = Counter(friends)

print(friends_count['Manthan'])
print(friends_count)


device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.0])
print(temperature_counter)
print(temperature_counter[16.0])