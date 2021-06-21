# list Comprehension

number = [1,2,3,4,5]
doubled_number = []
for num in number:
    doubled_number.append(num*2)
print(doubled_number)

# Using Comprehension
doubled_number = [num*3 for num in number]
print(doubled_number)

friend_marks = [100,39,80,90]
marks_string = [f"My Friend Got {marks} marks" for marks in friend_marks]
print(marks_string)

name = "Vishal"
print(name.lower())
print(name.upper())
print(name.title())

friend_names = ["Harsh","Sahil","Manthan","Sanjay"]
lower_case_name = [name.lower() for name in friend_names]
print(lower_case_name)

user_name = input("Enter Name: ")
friends = ["Harsh","Sahil","Manthan","Sanjay"]
friends_lower = [name.lower() for name in friends]
if user_name.lower() in friends_lower:
    print(f"I Know {user_name}")