# Comprehension with Condition
odd_even = [1,2,3,4,5,6,7,8]
odd = [num for num in odd_even if num % 2 == 1]
print(odd)

# 1.
friends_list = ["Harsh","Manthan","Sahil"]
guests_list  = ["Sanjay","Chirag","Sahil","Manthan"]
friends_list_lower = set(friends_list)
guests_list_lower = set(guests_list)

print(friends_list_lower.intersection(guests_list_lower))

# 2.
# -- nested list comprehensions --
# Don't do this, because it's almost completely unreadable.
# Splitting things out into variables is better.

present_friend = [name.title() for name in guests_list
                  if name.lower() in
                  [f.lower() for f in friends_list]]
print(present_friend)