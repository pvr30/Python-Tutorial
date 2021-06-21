
"""
any() : it gives true is there is atleast one element and
gives false if it is empty.
"""
print(any([1, 2, 3, 4, 5]))  # True
print(any([]))            # False


"""
all() : It gives true if 0 is not there 
"""
print(all([1, 2, 3, 4, 5]))  # True
print(all([0, 1, 2, 3]))    # False


b = -0.0
print(bool(b))

print(bool(0.00000000000000000000001))
print(bool([]))
print(bool([None]))


# We  can implement __bool__ method in our class

