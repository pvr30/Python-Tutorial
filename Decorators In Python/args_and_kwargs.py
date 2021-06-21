# *args

def add(a, b, c, d):
    return a+b+c+d

print(add(2, 3, 4, 5))

# Instaed Of Doing This For Multiple Arguments We Can Use *args

def add_arg(*args): # Here All Arguments Are In Separate Mode.
    return sum(args)   

print(add_arg(1, 2, 3))
print(add_arg(2, 3, 4, 5))
print(add_arg(*(1, 2, 3, 4, 5)))  # tuple 



# **kwargs : This Will UseFor Any Key Word Values.

def greet(**kwargs):
    for k, v in kwargs.items():
        print(f"Hello {v} ")

greet(name='Vishal', surname='Parmar')
