age = int(input("Enter Your Age: "))
print(age >= 18)   # It gives true or false.

# Magic number
number = 5
num = int(input("Enter Number: "))
matches = num == number
print(f"Your Assumption is  {matches}")

# AND
num = int(input("Enter Number: "))
random = num>=18  and  num<=65  # Both Condition Will Be True For true result .
print(random)  # Gives True And False

# OR
num = int(input("Enter Number: "))
random = num>=18 or num<=65  # Only One Condition Will Be True For true result .
print(random)  # Gives True And False

# bool

x = bool(35) # Here in bool some value ais there if 0 is there then it gives false.
y = bool("Hello")  # Same in string if string is null it gives false.
print(x)
print(y)

x = bool(0)
y = bool("")
print(x)
print(y)

x = True
print(x and 18)  # here if  left operand is true then it gives second operand.
print(x or 18)  # here if  left operand is true then it gives True.

age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or side_job)