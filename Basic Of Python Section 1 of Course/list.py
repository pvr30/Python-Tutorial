# List

friends = ["Harsh","Sahil","Manthan"]

print(friends[0])
print(friends[1])
print(friends[2])
print(len(friends))  # find length of the elements in list.

friends.append("Sanjay")

print(len(friends))  # 4

friends.append(20)
print(friends)   # ['Harsh', 'Sahil', 'Manthan', 'Sanjay', 20]

friends.remove(20)

print(friends)

# lists inside lists

friends_age = [["Harsh",21],["Sahil",18],["Manthan",19]]

print(friends_age[0])  # Here First List will print .
print(friends_age[0][0]) # Here First Element of first list will print.

friends_age.append("Sanjay")
print(friends_age)
# friends_age.remove("Sahil")
# If You Have a list of list then you have to remove whole list.

friends_age.remove(["Manthan",19])
print(friends_age)

# Scaling in List
print(friends[:3])
