"""
Decorator: Which Function is take a function as a parameter/argument and also return 
a function that type of function is called Decorator

"""
"""
user = {'username': 'jose123', 'access_level': 'admin'}

def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func
    
def my_function():
    return 'Password for admin panel is 1234.'

my_secure_function = user_has_permission(my_function)

print(my_secure_function())
"""


# another example.

def div(a, b):
    print(a/b)


def decorator(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner


div1 = decorator(div)

div1(2,4)
