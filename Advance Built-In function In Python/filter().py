# filter() function

"""
The `filter()` function is a built-in function in Python that you
can call from any file or program.

It takes two arguments:

* A function; and
* An iterable (now we know what these are!)

The function, which is the first argument, must return `True` or `False`.
It must also have one parameter which is the current element of the list we’re working with.

The list we’re working with is the second argument to the `filter()` function.

The `filter()` function then returns a generator of the elements for
which the first argument returns `True`.

"""

def check_friends(friend):
    return friend.startswith('H')

friends = ['Harsh', 'Manthan', 'Harish', 'Sahil']

start_with_H = filter(check_friends, friends)

print(start_with_H)
print(list(start_with_H))
print(list(start_with_H))

# Usually We use lambda function for filter.

names = ['Sahil', 'Manthan', 'Suresh', 'Sanjay', 'Chirag']
start_with_S = filter(lambda name: name.startswith('S'), names)

print(list(start_with_S))


# We can use Generator Comprehension instead of filter()

another_starts_with_S = (name for name in names if name.startswith('S'))

print(list(another_starts_with_S))

