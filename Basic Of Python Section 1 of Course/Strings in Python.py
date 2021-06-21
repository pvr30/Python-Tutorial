my_string = "Hello Python"
print(my_string)
my_string = 'Hello Python2'  # we can also use '' in python
print(my_string)
another_string = "Hello! 'What are you doing'."
print(another_string)
another_string = 'Hello ! "What are you doing". '
print(another_string)
first_string = "Vishal Parmar"
print("Hello "+first_string)
first_name = "Vishal"
greeting = "Hello" +  first_name
print(greeting)
another_greeting = f"How are You  {first_name} ?"  # This is called fstream .
# In f-strings, {name} gets replaced by the value of the variable name.
print(another_greeting)

# This is called format method .
# The {} gets replaced by whatever is inside the brackets of the .format()
final_greeting = "Hey What are you doing ? {}".format(first_name)
print(final_greeting)

# You can also give names to variables inside a formattable string:
friend_name = "Harsh"
goodbye = "Goodbye, {first_name}!"
goodbye_harsh = goodbye.format(first_name=friend_name)
print(goodbye_harsh)

greeting = "Hey How are you {} "
print(greeting.format(first_name))

# Usually you will be using f-strings, just because they are shorter and more readable.
# However sometimes you may need to re-use a format string, and that is when using .format() is useful.


# Multi-line String
name = "Rolf Smith"
street = "123 No Name Road"
postcode = "PY10 1CP"

address = f"""Name: {name}
Street: {street}
Postcode: {postcode}
Country: United Kingdom"""
print(address)

description = "{} is {age} years old."
print(description.format("Bob", age=30))

# Slicing in Python.

demo = "Vishal Parmar"
print(demo[:4])
print(demo[0:6])
print(demo[7:-1]) # here -1 is  r
print(demo[:-1])