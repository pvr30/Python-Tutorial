"""
deque : - Double Ended Queue

In a `deque`, we can push elements at the start or the end,
and we can also remove elements from the start or the end.

It is very efficient, performing very well.

"""

from collections import deque

friends = deque(('Harsh', 'Manthan', 'Sahil', 'Sanjay'))
print(friends)

friends.append('Chirag')
print(friends)

friends.appendleft('Manav')
print(friends)

friends.pop()
print(friends)

friends.popleft()
print(friends)

