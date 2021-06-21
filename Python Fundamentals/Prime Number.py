# Find Prime Number.
number = int(input("Enter A Number: "))
counter = 0
for n in range(1,number+1):
    if number % n == 0:
        counter += 1

if counter == 2:
    print("The Given Number Is Prime.")
else:
    print("The Given Number Is Not Prime.")

