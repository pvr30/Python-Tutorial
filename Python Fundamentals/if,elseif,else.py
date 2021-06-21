# if statement

number = 5
user_number = int(input("Enter A Number: "))
if user_number == number:
    print("Valid Number")
# In Python the four spaces before print is required
# These Space are called as Identation.

# if else
# Find Even or Odd Number.

user_number = int(input("Enter a Number: "))
if user_number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# elseif
# Positive Or Negative

user_number = int(input("Enter A Number: "))

if user_number > 0:
    print("Positive Number")
elif user_number < 0:
    print("Negative Number")
else:
    print("Zero")

# Using 'in' keyword for list.

local_friends = ["Harsh","Manthan","Sanjay"]
collage_friends = ["Sahil","Umang"]

user_name = input("Enter Name: ")

if user_name in local_friends:
    print("Hello Local Friend")
elif user_name in collage_friends:
    print("Hello Collage Friend")
else:
    print("I Don't Know You")