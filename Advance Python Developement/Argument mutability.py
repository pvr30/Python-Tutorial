friends = {
    'Harsh': 25,
    'Sahil': 18,
    'Manthan': 20
}


def change_data(friend, name):
    print(id(friend))
    friend[name] = 10

print(id(friends))
change_data(friends, 'Sahil')
print(id(friends))

# For all id we get same address.

print(id(friends['Manthan']))

change_data(friends, 'Manthan')

print(id(friends['Manthan']))


"""
As we can see the dictionary itself same address.
but the address of friends object have different addresses.


`friends` does not change before and after running the function,
but `friends['Manthan']` does change.

We used an `=` sign, and also `friends['Manthan']` is an integer 
which is an immutable type.

"""

# Another example:
age = 10

def change_age(age):
    current_age = age + 1

print(id(age))
change_age(age)
print(id(age))

# but if we do this..
age = age + 1
print(id(age))  # We get different address because integers are immutable


# another list example:

primes = [2, 3, 5]

print(id(primes))

primes += [7, 11]  # We know += is 'like' primes = primes + [7, 11]...

print(id(primes))

"""
You get the same `id` back!!!

That’s because `+=` is not `=`.

When you do `=`, this happens:
"""

primes = primes.__add__([7, 11])

"""
When you do `+=`, this happens:
"""

primes = primes.__iadd__([7, 11])

"""
Thus, it’s all up to whether `__add__` and `__iadd__` create new objects or 
modify the existing objects. It’s easy to check their implementations by doing this:


You can see that when we did `primes.__add__`, it did not change `primes`.

But when we did `primes.__iadd__`, it did change `primes`. Interesting stuff!

"""

