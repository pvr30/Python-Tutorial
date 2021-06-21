import time

def power(limit):
    return [x**2 for x in range(limit)]

start = time.time()
power(50000000)
end = time.time()
print(end-start)  # Gives around 43.5 seconds

"""
You could of course turn this into a function:
"""

import time

def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(50000000))   # this will take less time.



# timeit


import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("map(lambda x: x**2, range(10))"))

"""
This runs the statement a default of 10,000 times to check how long it runs for
Notice how list comprehension is faster than map()!

"""