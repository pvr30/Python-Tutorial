
"""
A namedtuple is another object that we can use like a tuple, where each of the elements
of the tuple has a name. In addition, the tuple itself also has a name.

It improves on tuples by making more explicit what it means.

"""
from collections import namedtuple

account = ('Harsh', 1900)

print(account[0])
print(account[1])

# instead of this we can give names to tuple element.

Account = namedtuple('Account', ['name', 'amount'])

account = Account('Manthan', 5000)

print(account.name)
print(account.amount)

print(account)   # Account(name='Manthan', amount=5000)

