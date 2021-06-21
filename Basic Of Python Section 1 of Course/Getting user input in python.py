your_name = input("Enter Your Name :")
print(f"Welcome {your_name}")

age = input("Enter Your Age: ")
age_num = int(age) # we can convert from string to int .
print(f"You Lived {age_num*12} months.")

# also we can use like below.
age = int(input("Enter Your age :"))
print(f"You Lived {age*12} months.")
# Here input("Enter Your age :") is become that value which is entered by user in th string form.
# Swap Two Numbers.

a = int(input("Enter Value Of a "))

b = int(input("Enter Value Of b "))

print(f"Before Swapping a={a} and b={b}")
a = a+b
b = a-b
a = a-b

print(f"After Swapping a={a} and b={b}")
