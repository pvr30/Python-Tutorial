# Argument Unpacking

friends_age = [
    ('Harsh', 25),
    ('Manthan', 39),
    ('Sahil', 20),
    ('Sanjay', 12)
]

for f in friends_age:
    print(f[0], f[1])

# Here we can use unpacking
print("\nAfter Unpacking")

for f in friends_age:
    print(*f)


# If The data is in dictionary format.

class friends:
    def __init__(self, Name, Branch):
        self.name = Name
        self.branch = Branch

    def __repr__(self):
        return f"{self.name} is in {self.branch} Branch"

friends_branch = [
    {'Name': 'Harsh', 'Branch': 'Medical'},
    {'Name': 'Sahil', 'Branch': 'ECE'},
    {'Name': 'Sanjay', 'Branch': 'MBA'}
]

friend_1 = [friends(**data) for data in friends_branch]

print(friend_1)


