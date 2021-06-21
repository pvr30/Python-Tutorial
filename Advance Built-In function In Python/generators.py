#  Generators:
"""
A generator in Python is a function that remembers the state it’s in, in between executions.

You have to run the function every time you want a new number,
that’s why it’s called a “generator”.
It generates numbers (or indeed strings, or anything else you want to generate).

The `yield` keyword is very much like a `return`, in that it gives the value back
to the caller and returns execution
control to them (show this with example run).
However, the next time you run the function,
execution continues from the very next line inside the function, instead of from the top.
"""

"""
def hundred_numbers():
    nums = []
    i = 0
    while i < 100:
        nums.append(i)
        i += 1
    return nums

print(hundred_numbers())

"""

"""
Instead Of Above code we can use generators.

"""
def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i += 1
    return i

g = hundred_numbers()

print(next(g))
print(next(g))
print(g)

for i in range(10):
    print(next(g))


print(list(g))

# Generate Prime Number

def prime_generator(bound):
    for n in range(2, bound):   # n starts from 2 to bound
        for x in range(2, n):   # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:   # if no such x is found after exhausting all 1<x<n
            yield n


g1 = prime_generator(20)

print(next(g1))