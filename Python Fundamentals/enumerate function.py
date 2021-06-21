# enumerate  function

friends = ["Harsh","Manthan","Sahil","Sanjay"]
i = 0
for friend in friends:
    print(i,friend)
    i = i + 1
# Instead Of This we can use enumerate.
print("\n")
for counter,friend in enumerate(friends):
    print(counter,friend)

print(list(enumerate(friends)))
print(dict(enumerate(friends)))

# We can start counter from our own number .
for counter,friend in enumerate(friends,start=1):
    print(counter,friend)
