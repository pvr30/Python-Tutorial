"""

typing is used to define/fixed the return type of function
as well as parameter type like in...
c++
int a=10 -or- int fun()

"""
from typing import List, Tuple

def add(a: int, b: int) -> int:
    return a+b

print(add(3, 4))

def num(n: int) -> List:
    num_list = []
    for i in range(n):
        num_list.append(i)
    return num_list

print(num(10))



